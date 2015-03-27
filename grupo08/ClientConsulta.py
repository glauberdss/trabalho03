#!/usr/bin/env python

from SOAPpy import SOAPProxy
from server import consultaFuncionario

servico = SOAPProxy("http://localhost:8008")

#codigo = raw_input('Codigo: ')

#if servico.consultaFuncionario(codigo):
#	print 'Este funcionario ja existe'
#else:
#	print 'O funcionario nao existe'



print 'selecione o codigo: '
codigo = raw_input('codigo da funcionario: ')
print servico.consultaFuncionario(codigo)
