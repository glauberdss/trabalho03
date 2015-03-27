#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8011")

codigoAreceber = raw_input('codigoAreceber: ')

if servico.consultarAreceber(codigoAreceber):
	print 'Codigo a receber existe'
else:
	print 'Codigo a receber nao existe'
