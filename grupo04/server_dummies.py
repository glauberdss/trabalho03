# -*- coding: utf-8 -*-

class ClienteEstoqueFake():

    def consultaEstoque(self, codigo_estoque):
        return codigo_estoque == 1

class ClienteProdutoFake():

    def consultaProduto(self, codigo_produto):
        if codigo_produto == 1:
            return {'codigo': 1,
                    'descricao': 'eisenbahn weizenbock',
                    'preco': 25,
                    'codigoFabricante': 1}
        else:
            return False
