# Generated by Django 4.2.4 on 2023-09-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_available_count',
            field=models.IntegerField(default=0),
        ),
    ]
