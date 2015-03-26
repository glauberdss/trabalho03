#-*- encoding: iso-8859-1 -*-

from SOAPpy import SOAPServer

db = 'clientes.txt'

def cadastraCliente(Cliente):
	conexao = open(db,'a')
	conexao.write('%s|%s|%s\n' % (Cliente['codigo'],Cliente['nome'], Cliente['contato']))
	conexao.close()
	return True
	
def deletarCliente(codigoCliente):
	conexao_r = open(db,"r")
	clientes_linhas = conexao_r.readlines()
	conexao_r.close()

	conexao_w = open(db,"w")
	for clientes_linhas in cliente_linha:
		codigo, nome, contato = cliente_linha.split('|')
		if codigo != codigoCliente:
			conexao_w.write(cliente_linha)
	conexao_w.close()
	return True


serv = SOAPServer(("localhost", 8006))

serv.registerFunction(cadastraCliente)
serv.registerFunction(deletarCliente)

serv.serve_forever()
