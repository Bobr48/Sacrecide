# Generated by Django 4.2.10 on 2024-05-06 19:18

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_merch_alter_history_text_alter_musicians_text'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='merch',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
