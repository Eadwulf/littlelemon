# Generated by Django 4.1.6 on 2023-02-06 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemon', '0020_alter_purchases_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='purchase',
        ),
        migrations.DeleteModel(
            name='Purchases',
        ),
    ]
