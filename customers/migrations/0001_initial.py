# Generated by Django 4.1.5 on 2023-01-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id_customer', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.TextField(max_length=50)),
                ('apellido_cliente', models.TextField(max_length=50)),
            ],
        ),
    ]