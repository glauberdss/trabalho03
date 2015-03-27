#-*- encoding: iso-8859-1 -*-

from SOAPpy import SOAPServer, SOAPProxy
from produto_no_estoque import ProdutoNoEstoque

server = SOAPServer(("localhost", 8004))
cliente_estoque = SOAPProxy("localhost", 8001)
cliente_produto = SOAPProxy("localhost", 8003)


def inserir_produto_no_estoque(codigo_estoque, codigo_produto, quantidade):
    ProdutoNoEstoque(
        codigo_estoque=codigo_estoque,
        codigo_produto=codigo_produto,
        quantidade=quantidade
    ).salvar()
    return True

def consultar_produto_em_estoque(codigo_produto, codigo_estoque):
    return ProdutoNoEstoque.verificar_quantidade(codigo_produto, codigo_estoque)

def consultar_estoque_do_produto(codigo_estoque):
    return True

def pesquisar_preco_do_produto(codigo_produto):
    return True

server.registerFunction(inserir_produto_no_estoque,
    funcName='inserirProdutoEstoque')
server.registerFunction(consultar_produto_em_estoque,
    funcName='consultaProdutoEmEstoque')
server.registerFunction(consultar_estoque_do_produto,
    funcName='consultaEstoqueEmProdutoEstoque')
server.registerFunction(pesquisar_preco_do_produto,
    funcName='pesquisaPrecoProdutoEstoque')
server.serve_forever()
