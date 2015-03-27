#!/usr/bin/env python

from SOAPpy import SOAPProxy
# from server import cadastraFuncionario

# conectando diretamente
servico = SOAPProxy("http://localhost:8008")

codigo = raw_input('codigo: ')
nome = raw_input('nome: ')
endereco = raw_input('endereco: ')
sexo = raw_input('sexo: ')
datanascimento = raw_input('datanascimento: ')

funcionario ={'codigo':codigo, 'nome':nome, 'endereco':endereco, 'sexo':sexo, 'datanascimento':datanascimento}

if servico.cadastraFuncionario(funcionario):
	print 'funcionario cadastrado com sucesso'
else:
	print ' Problemas ao cadastrar! Tente novamente'

