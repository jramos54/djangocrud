# Generated by Django 4.1.5 on 2023-01-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customers_email_alter_customers_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]