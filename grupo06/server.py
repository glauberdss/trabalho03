#-*- encoding: iso-8859-1 -*-

from SOAPpy import SOAPServer

from cliente import Cliente

db = 'clientes.txt'

def cadastraCliente(Cliente):
	conexao = open(db,'a')
    	conexao.write('%s|%s|%s\n' % (Cliente.codigo, Cliente.nome, Cliente.contato))
    	conexao.close()


serv = SOAPServer(("localhost", 8006))

serv.registerFunction(cadastraCliente)

serv.serve_forever()
