# Generated by Django 3.2.9 on 2021-12-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(max_length=50)),
                ('genre_name', models.CharField(max_length=20)),
            ],
        ),
    ]
