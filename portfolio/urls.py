from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("education", views.education_page, name="education_page"),
    path("skills", views.skills_page, name="skills_page"),
    path("contact", views.contact, name="contact"),

    path("favorites", views.favorites_hub, name="favorites_hub"),
    path("favorites/books", views.favorite_books, name="favorite_books"),
    path("favorites/music", views.favorite_music, name="favorite_music"),
    path("favorites/movies", views.favorite_movies, name="favorite_movies"),

    path("admin/login", views.login_view, name="login"),
    path("admin/logout", views.logout_view, name="logout"),
    path("admin", views.dashboard, name="dashboard"),

    path("admin/profile/update", views.update_profile, name="update_profile"),

    path("admin/education/add", views.add_education, name="add_education"),
    path("admin/education/delete/<int:item_id>", views.delete_education, name="delete_education"),

    path("admin/skills/add", views.add_skill, name="add_skill"),
    path("admin/skills/delete/<int:item_id>", views.delete_skill, name="delete_skill"),

    path("admin/favorites/add", views.add_favorite, name="add_favorite"),
    path("admin/favorites/delete/<int:item_id>", views.delete_favorite, name="delete_favorite"),

    path("admin/security/change-password", views.change_password, name="change_password"),
]
