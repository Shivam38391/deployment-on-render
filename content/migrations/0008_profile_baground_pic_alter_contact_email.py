# Generated by Django 4.1.1 on 2022-10-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0007_alter_contact_subject_alter_education_start_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="baground_pic",
            field=models.ImageField(default="", upload_to="profile/bg/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contact", name="email", field=models.EmailField(max_length=50),
        ),
    ]
