# Generated by Django 3.2 on 2021-04-27 12:54

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20210426_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoImagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Titulo')),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Identificador')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modificado em')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalogo.produto')),
            ],
            options={
                'verbose_name': 'produto_imagem',
                'verbose_name_plural': 'produto_imagens',
                'db_table': 'produto_imagem',
                'ordering': ('-created_at',),
            },
        ),
    ]