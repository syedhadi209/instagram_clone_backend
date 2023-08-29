# Generated by Django 4.2.4 on 2023-08-29 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0003_rename_attachment_storyattachement_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storyattachement",
            name="story",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="urls",
                to="stories.story",
            ),
        ),
    ]
