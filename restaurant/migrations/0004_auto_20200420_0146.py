# Generated by Django 3.0.5 on 2020-04-19 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menuitem_restaurant'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
