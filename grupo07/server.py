from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy


db = 'compra.txt'

def cadastrarCompra(Compra):
	if consultarCompra(Compra['codigoCompra']):
		return False
	conexao = open(db,'a')
	conexao.write('%s|%s|%s|%s|%s|%s\n' % (Compra['codigoCompra'],Compra['codigoProduto'], Compra['quantidade'], Compra['data'], Compra['valortotal'], Compra['codigoFornecedor']))
	conexao.close()
	return True

def deletarCompra(codigoCompra):
	try:

			f = open(db,"r")
			linhas = f.readlines()
			f.close()

			f = open(db,"w")
			for linha in linhas:
				codigoCompra_, codigoProduto, quantidade, data, valortotal, codigoFornecedor = linha.split('|')
				if codigoCompra != codigoCompra_:
					f.write(linha)
			f.close()

			return True
	except:
		return False

def consultarCompra(codigoCompra):
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()

		for linha in linhas:
			codigoCompra_, codigoProduto, quantidade, data, valortotal, codigoFornecedor = linha.split('|')
			if codigoCompra_ == codigoCompra:
				f.close()
				return True

		f.close()

		return False

	except:
		return False

def listarCompra():
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		return linhas
	except:
		return False

def consultaFornecedorExisteCompra(codigoFornecedor):
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()

		for linha in linhas:
			codigoCompra_, codigoProduto, quantidade, data, valortotal, codigoForn = linha.split('|')
			if codigoForn == codigoFornecedor:
				print'achou'
				return True

		f.close()

		return False

	except:
		return False




serv = SOAPServer(("localhost", 8007))

serv.registerFunction(consultarCompra)
serv.registerFunction(cadastrarCompra)
serv.registerFunction(deletarCompra)
serv.registerFunction(consultaFornecedorExisteCompra)


serv.serve_forever()

