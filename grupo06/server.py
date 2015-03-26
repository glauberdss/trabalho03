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

def consultarCliente(codigoCliente):
	try:	
		servico_venda = SOAPProxy("http://localhost:8009")
		vendas_linhas = servico_venda.listarVenda()
		
		for vendas_linhas in venda_linha:
			codigoVenda, codigoClienteVenda, codigoFuncionario, data, valortotal, codigoProduto, quantidadecodigoVenda, codigoCliente, codigoFuncionario, data, valortotal, codigoProduto, quantidade = venda_linha.split('|')
			if codigoClienteVenda == codigoCliente:
				return True
		return False
	except:
		return False

serv = SOAPServer(("localhost", 8006))

serv.registerFunction(cadastraCliente)
serv.registerFunction(deletarCliente)
serv.registerFunction(consultarCliente)

serv.serve_forever()
