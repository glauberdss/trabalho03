#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8011")

print 'Deletar cadastro'

codigoAreceber = raw_input('Codigo a Receber: ')

if servico.deletarAreceber(codigoAreceber):
	print 'Deletada com sucesso'
else:
	print 'Receber nao encontrada'

