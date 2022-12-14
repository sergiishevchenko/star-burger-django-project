# Generated by Django 3.2.15 on 2022-12-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, unique=True, verbose_name='Адрес')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта координат')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='Долгота координат')),
                ('update_date', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Когда был запрос')),
            ],
        ),
    ]