# Generated by Django 3.2.9 on 2022-01-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refer', '0002_alter_profile_identify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identify',
            field=models.BooleanField(default=False),
        ),
    ]
