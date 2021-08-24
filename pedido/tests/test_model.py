from django.test import TestCase
from django.contrib.auth.models import User
from usuario.models import Cliente
from pedido.models import Pedido, ItemPedido

from catalogo.tests.test_model import get_fake_produto
from usuario.tests.test_model import get_fake_endereco, get_fake_user
from catalogo.models import Modelo, ModeloProduto, ModeloVariacao, TipoVariacao, Variacao


class PedidoModelTest(TestCase):
    def setUp(self):
        self.obj = get_fake_pedido()

    def test_create(self):
        self.assertTrue(Pedido.objects.exists())


class ItemPedidoModelTest(TestCase):
    def setUp(self):
        pedido = get_fake_pedido()
        produto = get_fake_produto()
        modelo = Modelo.objects.create(descricao='T-Shirt')
        modelo_produto = ModeloProduto.objects.create(
            produto=produto, modelo=modelo)

        # Tamanho
        variacao_tamanho = Variacao.objects.create(descricao='Tamanho', )
        tipo_variacao_tamanho = TipoVariacao.objects.create(
            descricao='P', variacao=variacao_tamanho,)
        # Cor
        variacao_cor = Variacao.objects.create(descricao='Cor', )
        tipo_variacao_cor = TipoVariacao.objects.create(
            descricao='Amarelo', variacao=variacao_cor,)

        cor = ModeloVariacao.objects.create(
            modelo_produto=modelo_produto,
            tipo_variacao=tipo_variacao_cor,
            imagem='Imagem cloudinary',
        )
        tamanho = ModeloVariacao.objects.create(
            modelo_produto=modelo_produto,
            tipo_variacao=tipo_variacao_tamanho,
            imagem='Imagem cloudinary',
        )

        self.obj = ItemPedido.objects.create(
            pedido=pedido,
            produto=produto,
            tamanho=tamanho,
            cor=cor,
            modelo_produto=modelo_produto
        )

    def test_create(self):
        self.assertTrue(ItemPedido.objects.exists())
    
    def test_str(self):
        self.assertEqual('Camiseta NodeJs', str(self.obj))


def get_fake_pedido():
    user = get_fake_user('ronaldo', 'ronaldo@likeestampa.com.br')
    cliente = Cliente.objects.get(user=user)
    endereco_cliente = get_fake_endereco(cliente)
    return Pedido.objects.create(
        user=user,
        endereco_cliente=endereco_cliente,
    )
