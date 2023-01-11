# Generated by Django 4.1.1 on 2022-09-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("short_bio", models.CharField(max_length=50)),
                ("long_bio", models.CharField(max_length=250)),
                ("age", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("language", models.CharField(max_length=50)),
            ],
            options={"verbose_name": "About", "verbose_name_plural": "Abouts",},
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fullname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=20)),
                ("message", models.TextField()),
            ],
            options={"verbose_name": "Contact", "verbose_name_plural": "Contacts",},
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qualification", models.CharField(max_length=20)),
                ("start_date", models.CharField(max_length=20)),
                ("end_date", models.CharField(max_length=20)),
                ("degree", models.CharField(max_length=20)),
                ("institute", models.CharField(max_length=50)),
                ("descriptions", models.TextField()),
            ],
            options={"verbose_name": "Education", "verbose_name_plural": "Educations",},
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=20)),
                ("start_date", models.CharField(max_length=20)),
                ("end_date", models.CharField(max_length=20)),
                ("role", models.CharField(max_length=20)),
                ("responsibility", models.TextField()),
            ],
            options={
                "verbose_name": "Experience",
                "verbose_name_plural": "Experiences",
            },
        ),
        migrations.CreateModel(
            name="Personal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="portfolio/project1")),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=100)),
                ("link", models.CharField(max_length=150)),
            ],
            options={"verbose_name": "Personal", "verbose_name_plural": "Personals",},
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("profile_pic", models.ImageField(upload_to="profile/")),
                ("fullname", models.CharField(max_length=50)),
                ("designation", models.CharField(max_length=50)),
                ("cv", models.FileField(upload_to="profile/cv/")),
            ],
            options={"verbose_name": "Profile", "verbose_name_plural": "Profiles",},
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="reference/")),
                ("name_of_refer", models.CharField(max_length=50)),
                ("designation_refer", models.CharField(max_length=50)),
                ("words_of_refer", models.TextField()),
            ],
            options={"verbose_name": "Reference", "verbose_name_plural": "References",},
        ),
        migrations.CreateModel(
            name="SefPhotograph",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="portfolio/project1")),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=100)),
                ("link", models.CharField(blank=True, max_length=150)),
            ],
            options={
                "verbose_name": "SefPhotograph",
                "verbose_name_plural": "SefPhotographs",
            },
        ),
        migrations.CreateModel(
            name="Skill_1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pct", models.IntegerField()),
            ],
            options={"verbose_name": "Skill_1", "verbose_name_plural": "Skill_1s",},
        ),
        migrations.CreateModel(
            name="Skill_2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pct", models.IntegerField()),
            ],
            options={"verbose_name": "Skill_2", "verbose_name_plural": "Skill_2s",},
        ),
        migrations.CreateModel(
            name="Skill_3",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pct", models.IntegerField()),
            ],
            options={"verbose_name": "Skill_3", "verbose_name_plural": "Skill_3s",},
        ),
        migrations.CreateModel(
            name="Skill_4",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pct", models.IntegerField()),
            ],
            options={"verbose_name": "Skill_4", "verbose_name_plural": "Skill_4s",},
        ),
        migrations.CreateModel(
            name="Skill_5",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pct", models.IntegerField()),
            ],
            options={"verbose_name": "Skill_5", "verbose_name_plural": "Skill_5s",},
        ),
        migrations.CreateModel(
            name="Skill_6",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("pct", models.IntegerField()),
            ],
            options={"verbose_name": "Skill_6", "verbose_name_plural": "Skill_6s",},
        ),
        migrations.CreateModel(
            name="SocialMedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fb_link", models.CharField(max_length=50)),
                ("IG_link", models.CharField(max_length=50)),
                ("Linkedin_link", models.CharField(max_length=50)),
                ("twitter_link", models.CharField(max_length=50)),
                ("Google_link", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "SocialMedia",
                "verbose_name_plural": "SocialMedias",
            },
        ),
        migrations.CreateModel(
            name="Webdevelopment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="portfolio/project1")),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=100)),
                ("link", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "Webdevelopment",
                "verbose_name_plural": "Webdevelopments",
            },
        ),
    ]
