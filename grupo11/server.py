#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy

db = 'receber.txt'

def ContasArecebe(receber):
    if consultarAreceber(receber['codigoAreceber']):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s|%s|%s|%s\n' % (receber['codigoAreceber'],receber['codigoVenda'], receber['dataVencimento'], receber['dataPagamento'], receber['status']))
    conexao.close()
    return True

def consultarAreceber(pconsulta):
    try:
		linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		
		for linha in linhas:
			codigoAreceber,codigoVenda,dataVencimento,dataPagamento, status = linha.split('|')
			if ( pconsulta == codigoAreceber ):
				return True
		
		f.close()
		
		return False
        
    except:
        return False
        
def deletarAreceber(codigoR):
	try:
		servico = SOAPProxy("http://localhost:8011")
        
		f = open(db,"r")
		lines = f.readlines()
		f.close()
	
		f = open(db,"w")
		for linha in linhas:
			codigoAreceber,codigoVenda,dataVencimento,dataPagamento, status = linha.split('|')
			if codigoAreceber != codigoR:
				f.write(linha)
		f.close()
		return True
	except:
		return False

serv = SOAPServer(("localhost", 8011))

serv.registerFunction(ContasArecebe)
serv.registerFunction(consultarAreceber)
serv.registerFunction(deletarAreceber)
serv.serve_forever()
