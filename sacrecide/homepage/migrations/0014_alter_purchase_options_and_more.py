# Generated by Django 4.2.10 on 2024-05-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_alter_purchase_name_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['data']},
        ),
        migrations.AddIndex(
            model_name='purchase',
            index=models.Index(fields=['data'], name='homepage_pu_data_818b19_idx'),
        ),
    ]