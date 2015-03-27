#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8008")

codigo = raw_input('Codigo: ')

if servico.deletaFuncionario(codigo):
  print 'Funcionario excluido com sucesso'
else:
  print 'Problemas ao excluir! Tente novamente'