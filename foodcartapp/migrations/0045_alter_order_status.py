# Generated by Django 3.2.15 on 2022-12-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0044_auto_20221211_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'Необработанный'), ('IN_RESTAURANT', 'Передан в ресторан'), ('IN_WAY', 'Передан курьеру'), ('DONE', 'Выполнен')], db_index=True, default='IN_PROGRESS', max_length=20, verbose_name='Статус'),
        ),
    ]
