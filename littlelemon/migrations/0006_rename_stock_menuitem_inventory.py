# Generated by Django 4.1.5 on 2023-01-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemon', '0005_alter_menuitem_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='stock',
            new_name='inventory',
        ),
    ]
