# Generated by Django 3.2 on 2023-02-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_title_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=300, verbose_name='О себе'),
        ),
    ]
