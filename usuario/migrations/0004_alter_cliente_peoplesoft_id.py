# Generated by Django 3.2.4 on 2021-06-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_cliente_peoplesoft_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='peoplesoft_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]