# Generated by Django 4.1.4 on 2022-12-07 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0003_pet_trait"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pet",
            old_name="trait",
            new_name="traits",
        ),
    ]
