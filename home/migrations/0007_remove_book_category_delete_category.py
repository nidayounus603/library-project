# Generated by Django 4.1 on 2023-06-06 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_category_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]