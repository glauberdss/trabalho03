#!/usr/bin/env python

from SOAPpy import SOAPProxy

servico = SOAPProxy("http://localhost:8008")

codigo = raw_input('Codigo: ')

if servico.consultaFuncionario(codigo):
	print 'Este funcionario já existe'
	else:
		print 'O funcionario não existe'
