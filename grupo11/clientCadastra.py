#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
from os import fork
servico = SOAPProxy("http://localhost:8011")

print 'Cadastro de Receber'
codigoAreceber = raw_input('codigoAreceber: ')
codigoVenda = raw_input('codigoVenda: ')
dataVencimento = raw_input('dataVencimento: ')
dataPagamento = raw_input('dataPagamento: ')
status = raw_input('status: ')

receber ={'codigoAreceber':codigoAreceber,'codigoVenda':codigoVenda,'dataVencimento':dataVencimento,'dataPagamento':dataPagamento,'status':status}

if servico.ContasArecebe(receber):
	print 'Cadastrado com sucesso'
