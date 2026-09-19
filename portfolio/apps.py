from django.apps import AppConfig
from django.db.models.signals import post_migrate


def seed_defaults(sender, **kwargs):
    """
    Runs automatically after `python manage.py migrate`.
    Mirrors the original app's behaviour: create a default admin account
    and an (almost) empty profile row the first time the app is set up.
    """
    from django.conf import settings
    from django.contrib.auth import get_user_model
    from .models import Profile

    User = get_user_model()

    if not User.objects.exists():
        User.objects.create_superuser(
            username=settings.DEFAULT_ADMIN_USERNAME,
            email=settings.DEFAULT_ADMIN_EMAIL,
            password=settings.DEFAULT_ADMIN_PASSWORD,
        )

    if not Profile.objects.exists():
        Profile.objects.create(
            full_name="Umme Habiba",
            occupation="School Teacher",
            bio="",  # left blank on purpose — written from the admin panel
            profile_image="portfolio/images/habiba.jpg",
            email="",
            location="",
        )


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"

    def ready(self):
        post_migrate.connect(seed_defaults, sender=self)
