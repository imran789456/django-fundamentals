# Generated by Django 4.2.2 on 2023-07-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField()),
                ('movie_name', models.CharField(max_length=200)),
                ('hero', models.CharField(max_length=50)),
                ('herione', models.CharField(max_length=50)),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=10)),
            ],
        ),
    ]
