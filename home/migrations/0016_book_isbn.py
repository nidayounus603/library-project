# Generated by Django 4.2.3 on 2023-08-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=True, max_length=13),
        ),
    ]
