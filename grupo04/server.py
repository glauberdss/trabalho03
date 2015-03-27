# -*- coding: utf-8 -*-

from SOAPpy import SOAPServer, SOAPProxy
from produto_no_estoque import ProdutoNoEstoque, EstoqueFoiUsado
from server_dummies import ClienteProdutoFake, ClienteEstoqueFake

server = SOAPServer(("localhost", 8004))
ProdutoNoEstoque.cliente_produto = ClienteProdutoFake()
ProdutoNoEstoque.cliente_estoque = ClienteEstoqueFake()

def inserir_produto_no_estoque(codigo_estoque, codigo_produto, quantidade):
    return ProdutoNoEstoque(
        codigo_estoque=codigo_estoque,
        codigo_produto=codigo_produto,
        quantidade=quantidade
    ).salvar()

def consultar_produto_em_estoque(codigo_produto, codigo_estoque):
    return ProdutoNoEstoque.verificar_quantidade(codigo_produto, codigo_estoque)

def consultar_estoque_em_produto_estoque(codigo_estoque):
    return EstoqueFoiUsado(codigo_estoque).verificar()

def pesquisar_preco_do_produto(codigo_produto):
    return True

server.registerFunction(inserir_produto_no_estoque,
    funcName='inserirProdutoEstoque')
server.registerFunction(consultar_produto_em_estoque,
    funcName='consultaProdutoEmEstoque')
server.registerFunction(consultar_estoque_em_produto_estoque,
    funcName='consultaEstoqueEmProdutoEstoque')
server.registerFunction(pesquisar_preco_do_produto,
    funcName='pesquisaPrecoProdutoEstoque')
server.serve_forever()
