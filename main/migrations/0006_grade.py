# Generated by Django 3.2.9 on 2021-12-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_title', models.CharField(max_length=50)),
                ('grade_age', models.CharField(max_length=20)),
            ],
        ),
    ]