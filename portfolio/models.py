from django.db import models


class Profile(models.Model):
    """Singleton-style: the app always uses the first row."""

    full_name = models.CharField(max_length=100, default="Umme Habiba")
    occupation = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.CharField(
        max_length=255, blank=True,
        help_text="Static path, e.g. portfolio/images/habiba.jpg",
    )
    email = models.EmailField(max_length=150, blank=True)
    location = models.CharField(max_length=150, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Education(models.Model):
    LEVEL_CHOICES = [
        ("School", "School"),
        ("College", "College"),
        ("University", "University"),
        ("Degree/Other", "Degree / Other"),
    ]

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    institution_name = models.CharField(max_length=255)
    degree_title = models.CharField(max_length=150, blank=True)
    passing_year = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.level} — {self.institution_name}"


class Skill(models.Model):
    name = models.CharField(max_length=150)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.name


class Favorite(models.Model):
    CATEGORY_CHOICES = [
        ("Book", "Book"),
        ("Music", "Music"),
        ("Movie", "Movie"),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    subtitle_or_creator = models.CharField(max_length=200, blank=True)
    cover_image = models.CharField(max_length=255, blank=True)
    media_url = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    item_order = models.IntegerField(default=1)  # 1–4; first item = "Favourite" badge

    class Meta:
        ordering = ["category", "item_order", "id"]

    def __str__(self):
        return f"[{self.category}] {self.title}"
