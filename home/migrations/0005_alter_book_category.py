# Generated by Django 4.1 on 2023-06-06 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_category_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]