#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8082")

codigo = raw_input('Codigo: ')

if servico.consultaFabricante(codigo):
	print 'Este fabricante existe'
else:
	print 'O fabricante informado nao existe!'
