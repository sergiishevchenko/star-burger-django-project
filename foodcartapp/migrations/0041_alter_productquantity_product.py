# Generated by Django 3.2.15 on 2022-12-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0040_alter_productquantity_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productquantity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodcartapp.product'),
        ),
    ]
