# Generated by Django 4.1.3 on 2023-01-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='cantidad_pago',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='payments',
            name='cantidad_producto',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='payments',
            name='producto',
            field=models.TextField(max_length=30),
        ),
    ]
