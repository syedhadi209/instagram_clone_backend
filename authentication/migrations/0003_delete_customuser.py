# Generated by Django 4.2.4 on 2023-08-21 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_alter_customuser_username"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
