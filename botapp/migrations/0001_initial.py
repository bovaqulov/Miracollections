# Generated by Django 5.1 on 2024-08-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.BigIntegerField()),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
