#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8082")

codigo = raw_input('Codigo: ')
descricao = raw_input('Descricao: ')
localizacao = raw_input('Localizacao: ')

fabricante = {'codigo':codigo,'descricao':descricao,'localizacao':localizacao}

if servico.cadastraFabricante(fabricante):
    print 'Fabricante cadastrado com sucesso'
else:
    print 'Problemas ao cadastrar! Tente novamente'
