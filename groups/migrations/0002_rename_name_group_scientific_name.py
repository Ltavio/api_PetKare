# Generated by Django 4.1.4 on 2022-12-07 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="name",
            new_name="scientific_name",
        ),
    ]
