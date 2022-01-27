# Generated by Django 3.2.9 on 2022-01-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Name', models.CharField(max_length=15)),
                ('Price', models.IntegerField(default=True)),
                ('Ratings', models.IntegerField()),
                ('Number', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
