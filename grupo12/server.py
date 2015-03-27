#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy

db = 'comissao.txt'

def cadastraComissao(comissao):
    if consultarComissaoFuncionario(comissao['codigoFuncionario'], comissao['ano'], comissao['mes']):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s|%s|%s|%s\n' % (comissao['codigoComissao'],comissao['codigoFuncionario'], comissao['ano'], comissao['mes'], comissao['valor']))
    conexao.close()
    return True

def consultarComissaoFuncionario(pcodigoFun,pano,pmes):
    try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		
		for linha in linhas:
			codigoComissao,codigoFuncionario,ano,mes, valor = linha.split('|')
			if ( pcodigoFun == codigoFuncionario ) & ( pano == ano ) & ( pmes == mes ):
				return True
		
		f.close()
		
		return False
        
    except:
        return False

def calcularComissao(pcodigoFun,pano,pmes):
    linhas = open(db,'r').read()
    f = open(db,"r")
    linhas = f.readlines()	

    pvalor = 0

    for linha in linhas:
		codigoComissao,codigoFuncionario,ano,mes, valor = linha.split('|')
		if ( pcodigoFun == codigoFuncionario ) & ( pano == ano ) & ( pmes == mes ):
		     pvalor =pvalor + float(valor) 		

    f.close()
         
    return pvalor
        
    

def deletaComissaoFuncionario(pcodigoFun, pano, pmes):
	try:
		servico = SOAPProxy("http://localhost:8012")
        
		f = open(db,"r")
		lines = f.readlines()
		f.close()
	
		f = open(db,"w")
		for linha in linhas:
			codigoComissao,codigoFuncionario,ano,mes,valor = linha.split('|')
			if codigoFuncionario != pcodigoFun:
				f.write(linha)
		f.close()
		return True
	except:
		return False


def listaComissao():
	try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		return linhas
	except:
		return False


serv = SOAPServer(("localhost", 8012))

serv.registerFunction(cadastraComissao)
serv.registerFunction(consultarComissaoFuncionario)
serv.registerFunction(deletaComissaoFuncionario)
serv.registerFunction(listaComissao)
serv.registerFunction(calcularComissao)
serv.serve_forever()
