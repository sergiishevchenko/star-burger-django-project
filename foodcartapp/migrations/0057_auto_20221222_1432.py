# Generated by Django 3.2.15 on 2022-12-22 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0056_auto_20221222_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productquantity',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='foodcartapp.order'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='foodcartapp.product'),
        ),
    ]
