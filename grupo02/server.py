#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy

db = 'fabricante.txt'

def cadastraFabricante(fabricante):
    if consultaFabricante(fabricante['codigo']):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s|%s\n' % (fabricante['codigo'],fabricante['descricao'], fabricante['localizacao']))
    conexao.close()
    return True
    
def deleteFabricante(codigoFabricante):
	try:
	
		servico = SOAPProxy("http://localhost:8083")
		produtos = servico.listarProduto()
		
		existe = False
		
		for linha in linhas:
			codigo, descricao, preco, codigoFabricante_ = linha.split('|')
			if codigoFabricante == codigoFabricante_:
				existe = True

		if existe is False:
	
			f = open(db,"r")
			linhas = f.readlines()
			f.close()
	
			f = open(db,"w")
			for linha in linhas:
				codigo, descricao, localizacao = linha.split('|')
				if codigo != codigoFabricante:
					f.write(linha)
			f.close()

			return True
	except:
		return False

def consultaFabricante(codigoFabricante):
    try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		
		for linha in linhas:
			codigo, descricao, localizacao = linha.split('|')
			if codigoFabricante == codigo:
				return True
		
		f.close()
		
		return False
        
    except:
        return False
        
def listaFabricantes():
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		return linhas
	except:
		return False


serv = SOAPServer(("localhost", 8082))

serv.registerFunction(consultaFabricante)
serv.registerFunction(cadastraFabricante)
serv.registerFunction(deleteFabricante)
serv.registerFunction(listaFabricantes)

serv.serve_forever()
