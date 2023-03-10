# Generated by Django 4.1.6 on 2023-02-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemon', '0009_alter_cartitem_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.ManyToManyField(related_name='cart_item', to='littlelemon.cartitem'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cartitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cartitem', to='littlelemon.cartitem'),
        ),
    ]
