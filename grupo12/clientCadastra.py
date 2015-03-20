#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8012")

print 'Cadastro de Comissao'
codigoComissao = raw_input('Codigo da Comissao: ')
codigoFuncionario = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')
valor = raw_input('Valor: ')

comissao ={'codigoComissao':codigoComissao,'codigoFuncionario':codigoFuncionario,'ano':ano,'mes':mes,'valor':valor}

if servico.cadastraComissao(comissao):
	print 'Cadastrado com sucesso'
