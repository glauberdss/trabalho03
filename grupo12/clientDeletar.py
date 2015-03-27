#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8012")

print 'Deletar cadastro'

codigoFuncionario = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')
if servico.deletaComissaoFuncionario(codigoFuncionario, ano, mes):
	print 'Deletada com sucesso'
else:
	print 'Comissao nao encontrada'

