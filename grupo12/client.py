#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8001")

print 'Cadastrado de Comissao'
codigoComissao = raw_input('Codigo da Comissao: ')
codigoFuncionario = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')
valor = raw_input('Valor: ')

comissao ={'codigoComissao':codigoComissao,'codigoFuncionario':codigoFuncionario,'ano':ano,'mes':mes,'valor':valor}

if servico.cadastraComissao(comissao):
	print 'Cadastrado com sucesso'
print 'Deletar cadastro'

codigoFuncionario = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')
if servico.deletaComissaoFuncionario(codigoFuncionario,ano,mes):
	print 'Deletada com sucesso'
else:
	print 'Comissao nao encontrada'


print 'Digite o codigo pra consulta, retorno sera codigoComissao|codigoFuncionario|ano|mes|valor'
codigoFuncionario = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')
print servico.consultarComissaoFuncionario(codigoFuncionario,ano,mes    )

#if servico.login(user):
##    print 'Login efetuado com sucesso'
#else:
#    print 'O usuario nao existe ainda, cadastrando'
#    servico.registra(user)
