# Generated by Django 3.2.9 on 2022-01-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_alter_plo_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plo',
            name='company',
        ),
    ]
