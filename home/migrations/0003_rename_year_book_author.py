# Generated by Django 4.1 on 2023-06-03 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_book_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='year',
            new_name='author',
        ),
    ]