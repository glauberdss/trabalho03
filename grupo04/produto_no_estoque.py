# -*- coding: utf-8 -*-
import json
from SOAPpy import SOAPProxy

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
    cliente_estoque = SOAPProxy("localhost", 8001)
    cliente_produto = SOAPProxy("localhost", 8003)

    def salvar(self):
        if self.eh_valido():
            DB().adicionar(self)
        return self.eh_valido()

    def eh_valido(self):
        return self._estoque_existe() and self._produto_existe()

    def _estoque_existe(self):
        return self.cliente_estoque.consultaEstoque(self['codigo_estoque'])

    def _produto_existe(self):
        return self.cliente_produto.consultaProduto(self['codigo_produto'])

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
