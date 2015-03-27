# -*- coding: utf-8 -*-

class ClienteEstoqueFake():

    def consultaEstoque(self, codigo_estoque):
        return codigo_estoque == 1

class ClienteProdutoFake():

    def consultaProduto(self, codigo_produto):
        return codigo_produto == 1
