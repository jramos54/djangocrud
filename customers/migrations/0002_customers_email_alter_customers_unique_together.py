# Generated by Django 4.1.5 on 2023-01-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='email',
            field=models.EmailField(default='correo@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='customers',
            unique_together={('nombre_cliente', 'apellido_cliente', 'email')},
        ),
    ]
