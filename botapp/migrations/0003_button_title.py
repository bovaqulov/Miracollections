# Generated by Django 5.1 on 2024-08-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0002_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='title',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
