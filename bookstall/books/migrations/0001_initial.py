# Generated by Django 5.0.1 on 2024-01-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('published_year', models.IntegerField()),
                ('prize', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('pages', models.IntegerField()),
            ],
        ),
    ]
