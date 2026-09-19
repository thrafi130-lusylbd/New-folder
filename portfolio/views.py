from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile, Education, Skill, Favorite


def get_profile():
    return Profile.objects.first()


# ---------------------------------------------------------------------------
# Public pages
# ---------------------------------------------------------------------------

def index(request):
    profile = get_profile()
    first_name = (profile.full_name if profile else "Umme Habiba").split(" ")[0]
    return render(request, "portfolio/home.html", {
        "profile": profile,
        "first_name": first_name,
    })


def about(request):
    return render(request, "portfolio/about.html", {"profile": get_profile()})


def education_page(request):
    education = Education.objects.all()
    return render(request, "portfolio/education.html", {
        "profile": get_profile(),
        "education": education,
    })


def skills_page(request):
    skills = Skill.objects.all()
    return render(request, "portfolio/skills.html", {
        "profile": get_profile(),
        "skills": skills,
    })


def contact(request):
    return render(request, "portfolio/contact.html", {"profile": get_profile()})


def favorites_hub(request):
    return render(request, "portfolio/favorites_hub.html", {"profile": get_profile()})


def favorite_books(request):
    items = Favorite.objects.filter(category="Book")
    return render(request, "portfolio/books.html", {"profile": get_profile(), "items": items})


def favorite_music(request):
    items = Favorite.objects.filter(category="Music")
    return render(request, "portfolio/music.html", {"profile": get_profile(), "items": items})


def favorite_movies(request):
    items = Favorite.objects.filter(category="Movie")
    return render(request, "portfolio/movies.html", {"profile": get_profile(), "items": items})


# ---------------------------------------------------------------------------
# Admin auth
# ---------------------------------------------------------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    return render(request, "portfolio/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return redirect("login")


# ---------------------------------------------------------------------------
# Admin dashboard
# ---------------------------------------------------------------------------

@login_required
def dashboard(request):
    return render(request, "portfolio/admin_dashboard.html", {
        "profile": get_profile(),
        "education": Education.objects.all(),
        "skills": Skill.objects.all(),
        "favorites": Favorite.objects.all(),
    })


@login_required
def update_profile(request):
    if request.method == "POST":
        profile = get_profile()
        profile.full_name = request.POST.get("full_name", "").strip()
        profile.occupation = request.POST.get("occupation", "").strip()
        profile.bio = request.POST.get("bio", "").strip()
        profile.email = request.POST.get("email", "").strip()
        profile.location = request.POST.get("location", "").strip()
        profile.save()
        messages.success(request, "Profile updated.")
    return redirect("dashboard")


@login_required
def add_education(request):
    if request.method == "POST":
        Education.objects.create(
            level=request.POST.get("level"),
            institution_name=request.POST.get("institution_name", "").strip(),
            degree_title=request.POST.get("degree_title", "").strip(),
            passing_year=request.POST.get("passing_year", "").strip(),
            description=request.POST.get("description", "").strip(),
            display_order=int(request.POST.get("display_order") or 0),
        )
        messages.success(request, "Education entry added.")
    return redirect("dashboard")


@login_required
def delete_education(request, item_id):
    get_object_or_404(Education, id=item_id).delete()
    messages.success(request, "Education entry removed.")
    return redirect("dashboard")


@login_required
def add_skill(request):
    if request.method == "POST":
        name = request.POST.get("skill_name", "").strip()
        if name:
            Skill.objects.create(
                name=name,
                display_order=int(request.POST.get("display_order") or 0),
            )
            messages.success(request, "Skill added.")
        else:
            messages.error(request, "Skill name can't be empty.")
    return redirect("dashboard")


@login_required
def delete_skill(request, item_id):
    get_object_or_404(Skill, id=item_id).delete()
    messages.success(request, "Skill removed.")
    return redirect("dashboard")


@login_required
def add_favorite(request):
    if request.method == "POST":
        Favorite.objects.create(
            category=request.POST.get("category"),
            title=request.POST.get("title", "").strip(),
            subtitle_or_creator=request.POST.get("subtitle_or_creator", "").strip(),
            media_url=request.POST.get("media_url", "").strip(),
            description=request.POST.get("description", "").strip(),
            item_order=int(request.POST.get("item_order") or 1),
        )
        messages.success(request, "Favorite added.")
    return redirect("dashboard")


@login_required
def delete_favorite(request, item_id):
    get_object_or_404(Favorite, id=item_id).delete()
    messages.success(request, "Favorite removed.")
    return redirect("dashboard")


@login_required
def change_password(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password", "")
        new_password = request.POST.get("new_password", "")

        if not request.user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
        elif len(new_password) < 8:
            messages.error(request, "New password must be at least 8 characters.")
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)  # keep the session logged in
            messages.success(request, "Password updated.")
    return redirect("dashboard")
