from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(default="Umme Habiba", max_length=100)),
                ("occupation", models.CharField(blank=True, max_length=150)),
                ("bio", models.TextField(blank=True)),
                ("profile_image", models.CharField(blank=True, help_text="Static path, e.g. portfolio/images/habiba.jpg", max_length=255)),
                ("email", models.EmailField(blank=True, max_length=150)),
                ("location", models.CharField(blank=True, max_length=150)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("level", models.CharField(choices=[("School", "School"), ("College", "College"), ("University", "University"), ("Degree/Other", "Degree / Other")], max_length=20)),
                ("institution_name", models.CharField(max_length=255)),
                ("degree_title", models.CharField(blank=True, max_length=150)),
                ("passing_year", models.CharField(blank=True, max_length=20)),
                ("description", models.TextField(blank=True)),
                ("display_order", models.IntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "id"]},
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150)),
                ("display_order", models.IntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "id"]},
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("category", models.CharField(choices=[("Book", "Book"), ("Music", "Music"), ("Movie", "Movie")], max_length=10)),
                ("title", models.CharField(max_length=200)),
                ("subtitle_or_creator", models.CharField(blank=True, max_length=200)),
                ("cover_image", models.CharField(blank=True, max_length=255)),
                ("media_url", models.CharField(blank=True, max_length=255)),
                ("description", models.TextField(blank=True)),
                ("item_order", models.IntegerField(default=1)),
            ],
            options={"ordering": ["category", "item_order", "id"]},
        ),
    ]
