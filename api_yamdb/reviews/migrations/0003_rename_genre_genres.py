# Generated by Django 3.2 on 2023-01-31 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='Genres',
        ),
    ]