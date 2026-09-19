from django.contrib import admin

from .models import Profile, Education, Skill, Favorite

# Registered so the same data is also reachable from Django's own built-in
# admin at /django-admin/ if you ever want it — the custom /admin dashboard
# (styled to match the site) is what the public-facing "Admin" link uses.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Favorite)
