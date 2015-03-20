#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8082")

codigo = raw_input('Codigo: ')

if servico.deleteFabricante(codigo):
    print 'Fabricante excluido com sucesso'
else:
    print 'Problemas ao excluir! Tente novamente'
