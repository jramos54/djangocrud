# Generated by Django 4.1.5 on 2023-01-07 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customers_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='correo',
        ),
    ]
