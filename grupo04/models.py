# -*- coding: utf-8 -*-
import json
from SOAPpy import SOAPProxy
from server_dummies import ClienteProdutoFake, ClienteEstoqueFake

class Servicos():
    # habilita serviços fake para testes
    #estoque = SOAPProxy("localhost", 8001)
    #produto = SOAPProxy("localhost", 8003)
    estoque = ClienteEstoqueFake()
    produto = ClienteProdutoFake()

class DB(list):

    def __init__(self, *args, **kwargs):
        super(DB, self).__init__(*args, **kwargs)
        self.extend(json.load(open('DB', 'rb')))

    def adicionar(self, item):
        self.append(item)
        json.dump(self, open('DB', 'wb'))
        return self

    def procurar(self, match):
        return filter(match, self)


class ProdutoNoEstoque(dict):

    def salvar(self):
        if self.eh_valido():
            DB().adicionar(self)
        return self.eh_valido()

    def eh_valido(self):
        return self._estoque_existe() and self._produto_existe()

    def _estoque_existe(self):
        return Servicos.estoque.consultaEstoque(self['codigo_estoque'])

    def _produto_existe(self):
        return Servicos.produto.consultaProduto(self['codigo_produto'])

    @classmethod
    def verificar_quantidade(cls, codigo_produto, codigo_estoque):
        resultado = DB().procurar(
            lambda item: (
                [codigo_produto, codigo_estoque] ==
                [item['codigo_produto'], item['codigo_estoque']]
            )
        )
        return resultado[0]['quantidade'] if resultado else 0


class EstoqueFoiUsado():

    def __init__(self, codigo_estoque):
        self.codigo_estoque = codigo_estoque

    def verificar(self):
        return len(DB().procurar(
            lambda item: (self.codigo_estoque == item['codigo_estoque'])
        )) != 0


class PrecoDoProduto():

    def __init__(self, codigo_produto):
        self.codigo_produto = codigo_produto

    def consultar(self):
        produto = Servicos.produto.consultaProduto(self.codigo_produto)
        return produto['preco'] if produto else 0
