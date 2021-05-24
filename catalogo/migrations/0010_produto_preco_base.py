# Generated by Django 3.2 on 2021-05-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_alter_subcategoria_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco_base',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=999, verbose_name='Preço base'),
        ),
    ]
