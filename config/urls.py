from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("django-admin/", admin.site.urls),  # Django's built-in admin (separate from our /admin panel)
    path("", include("portfolio.urls")),
]
