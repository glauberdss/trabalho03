#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy

db = 'fornecedor.txt'

def cadastraFornecedor(Fornecedor):
	if consultaFornecedor(Fornecedor['codigo']):
		return False
	conexao = open(db,'a')
	conexao.write('%s|%s|%s\n' % (Fornecedor['codigo'],Fornecedor['nome'], Fornecedor['contato']))
	conexao.close()
	return True

def deletarFornecedor(codigoFornecedor):
	try:
	
		servico = SOAPProxy("http://localhost:8007")


		#acreditando que o servico retorne true ou false
		if servico.consultaFornecedorExisteCompra(codigoFornecedor):
			return False
		else:

			f = open(db,"r")
			linhas = f.readlines()
			f.close()

			f = open(db,"w")
			for linha in linhas:
				codigo, nome, contato = linha.split('|')
				if codigo != codigoFornecedor:
					f.write(linha)
			f.close()

			return True
	except:
		return False

def consultaFornecedor(codigoFornecedor):
	try:

		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		
		for linha in linhas:
			codigo, nome, contato = linha.split('|')
			if codigoFornecedor == codigo:
				f.close()
				return True
		
		f.close()
		
		return False

	except:
		return False

def listarFornecedor():
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		f.close()
		return linhas
	except:
		return False


serv = SOAPServer(("localhost", 8005))

serv.registerFunction(consultaFornecedor)
serv.registerFunction(cadastraFornecedor)
serv.registerFunction(deletarFornecedor)
serv.registerFunction(listarFornecedor)

serv.serve_forever()

