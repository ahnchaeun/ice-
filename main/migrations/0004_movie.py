# Generated by Django 3.2.9 on 2021-12-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211208_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_Title', models.CharField(max_length=50)),
                ('movie_Year', models.CharField(max_length=20)),
            ],
        ),
    ]
