#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy


db = 'produto.txt'

def cadastrarProduto(Produto):
	if consultaFabricante(Produto['codigoFabricante']):
		return False
	conexao = open(db,'a')
	conexao.write('%s|%s|%s\n' % (Produto['codigo'],Produto['descricao'], Produto['nome'], Produto['preco'], Produto['codigoFabricante']))
	conexao.close()
	return True


def consultaFabricante(codigoFabricante):
    try:
        servico = SOAPProxy("http://localhost:8002")

        #supondo que a funcao retorne true ou false
        if servico.consultaFabricante(codigoFabricante):
            return True

    except:
		return False

def deletarProduto(codigoProduto):
	try:
	
		servico = SOAPProxy("http://localhost:8004")


        #acreditando que o servico retorne true ou false
		if servico.consultaProdutoEmEstoque(codigoProduto) is False:
	
			f = open(db,"r")
			linhas = f.readlines()
			f.close()
	
			f = open(db,"w")
			for linha in linhas:
				codigo, nome, contato = linha.split('|')
				if codigo != codigoProduto:
					f.write(linha)
			f.close()

			return True
	except:
		return False

def consultaProduto(codigoProduto):
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		
		for linha in linhas:
			codigo, descricao, preco, codigoFabricante = linha.split('|')
			if codigoProduto == codigo:
				return True
		
		f.close()
		
		return False

	except:
		return False

def listarProduto():
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		return linhas
	except:
		return False


serv = SOAPServer(("localhost", 8003))

serv.registerFunction(consultaProduto)
serv.registerFunction(cadastrarProduto)
serv.registerFunction(deletarProduto)
serv.registerFunction(listarProduto)

serv.serve_forever()

