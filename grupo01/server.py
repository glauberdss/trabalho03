#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

from SOAPpy import SOAPServer
db = 'estoque.txt'


def cadastrarEstoque(estoque): 
    conexao = open(db,'a')
    conexao.write('%s|%s|%s\n' % (estoque.codigo,estoque.descricao, estoque.localizacao))
    conexao.close()
    return True
def deleteEstoque(codigo):
    servico = SOAPProxy("http://localhost:8004")
    try:
        linhas = open(db,'r').read()
    except:
        return False
    newarq = ''
    flag = 0

    if consultaProdutoEmEstoque(codigo):
        for linha in linhas.split('\n'):
            arq = linha.split('|')
            if arq[0] != codigo:
               newarq = newarq + '\n' + linha
            if arq[0] == codigo:
                flag = 1
        if flag == 0:
            return False
        else:
            open(db,'w').write(newarq)
        return True
    else:
            return False
def listaEstoque():
    try:
        linhas = open(db,'r').read()
    except:
        return False
    retorno = 'teste'
    for linha in linhas.split('\n'):
        retorno = retorno + linha 
    return retorno
    
def consultaEstoque(codigoEstoque):
    try:
        linhas = open(db,'r').read()
    except:
        return False
    retorno = 'Produto nao encontrado'
    for linha in linhas.split('\n'):
        estoque = linha.split('|')
        if (estoque[0] == codigoEstoque):
            retorno  = estoque[1]+' com codigo '+estoque[0]+' localizacao'+ estoque[2]
    return retorno


serv = SOAPServer(("localhost", 8001))

serv.registerFunction(cadastrarEstoque)
serv.registerFunction(deleteEstoque)
serv.registerFunction(listaEstoque)
serv.registerFunction(consultaEstoque)
serv.serve_forever()