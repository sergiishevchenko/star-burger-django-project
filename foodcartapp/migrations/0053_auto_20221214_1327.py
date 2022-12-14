# Generated by Django 3.2.15 on 2022-12-14 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0052_auto_20221212_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('UNPROCESSED', 'Необработанный'), ('IN_PROGRESS', 'В процессе выполнения'), ('DONE', 'Выполнен')], db_index=True, default='IN_PROGRESS', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_quantity', to='foodcartapp.order'),
        ),
    ]
