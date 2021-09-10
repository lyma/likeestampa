# Generated by Django 3.2.5 on 2021-09-10 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0054_produtoimagem'),
        ('checkout', '0011_rename_modelo_itemcarrinho_modelo_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='cor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_cor', to='catalogo.cor'),
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='tamanho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_tamanho', to='catalogo.tamanho'),
        ),
    ]

    run_before = [
        ('catalogo', '0055_auto_20210910_1354'),
    ]
