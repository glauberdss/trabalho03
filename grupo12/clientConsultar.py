#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8012")

codigoFun = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')

if servico.consultarComissaoFuncionario(codigoFun,ano,mes):
	print 'Esta Comissao existe'
else:
	print 'O comissao informado nao existe!'
