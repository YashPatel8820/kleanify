# Generated by Django 3.2.9 on 2022-01-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_alter_tally_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plo',
            name='file',
            field=models.FileField(blank=True, default='', null=True, upload_to='in/'),
        ),
    ]
