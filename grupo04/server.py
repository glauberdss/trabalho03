# -*- coding: utf-8 -*-

from SOAPpy import SOAPServer, SOAPProxy
from models import ProdutoNoEstoque, EstoqueFoiUsado, PrecoDoProduto

server = SOAPServer(("localhost", 8004))

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
    return PrecoDoProduto(codigo_produto).consultar()

server.registerFunction(inserir_produto_no_estoque,
    funcName='inserirProdutoEstoque')
server.registerFunction(consultar_produto_em_estoque,
    funcName='consultaProdutoEmEstoque')
server.registerFunction(consultar_estoque_em_produto_estoque,
    funcName='consultaEstoqueEmProdutoEstoque')
server.registerFunction(pesquisar_preco_do_produto,
    funcName='pesquisaPrecoProduto')
server.serve_forever()
