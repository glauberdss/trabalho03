#-*- encoding: iso-8859-1 -*-

from SOAPpy import SOAPServer
from SOAPpy import SOAPProxy

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

#	Impossibilidade de consulta:
#		Foi observado que, aparentemente, não é possível realizar uma consulta de uma forma que satisfaça a solicitação de desenvolvimento do metodo "consultarCliente(codigoCliente)".
#		Para desenvolver o metodo citato é necessário realizar uma consulta as vendas realizadas ,uma vez que o metodo, conforme solicitado, deve "Verificar se Cliente esta em algum venda".
#		Foi pedido ao grupo 9 (vendas), que seja feito os metodos "cadastrarVenda(Venda)", "consultarVenda(codigoVenda)" e "deletarVenda(codigoVenda)", como nosso metodo recebe apenas o "codigoCliente" como parametro e não existe um metodo "listarVenda" no webservice de vendas, não é possível verificar se o cliente está em alguma venda.
#		Da forma como foi solicitado, nosso grupo teria que ter conhecimento de TODOS os codigos de venda para consultar um a um para comparar.
#		Abaixo, desenvolvemos o metodo "consultarCliente" como se existisse um "listarVenda" no webservice de vendas, como sujestão de correção da impossibilidade.
#
#		Esse é o metodo listarVenda que acreditamos que deveria existir no webservice de vendas.
#		
#def listarVenda():
#	try:
#		conexao_r = open(db,"r")
#		vendas_linhas = conexao_r.readlines()
#		conexao_r.close()
#		return vendas_linhas
#	except:
#		return False

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
