#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8001")

print 'Cadastrado do Estoque'
codigo = raw_input('Codigo: ')
descricao = raw_input('Descricao: ')
localizacao = raw_input('Localizacao: ')

estoque ={'codigo':codigo,'descricao':descricao,'localizacao':localizacao}

if servico.cadastrarEstoque(estoque):
	print 'Cadastrado com sucesso'
print 'Deletar do estoque'
deletecodigo = raw_input('Codigo: ')
if servico.deleteEstoque(deletecodigo):
	print 'Deletado com sucesso'
else:
	print 'Produto nao encontrado'

retorno = servico.listaEstoque()
print retorno 
print 'Digite o codigo pra consulta, retorno sera codigo|descricao|localizacao'
consultacodigo = raw_input('Codigo: ')
print servico.consultaEstoque(consultacodigo)

#if servico.login(user):
##    print 'Login efetuado com sucesso'
#else:
#    print 'O usuario nao existe ainda, cadastrando'
#    servico.registra(user)