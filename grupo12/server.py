#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer
from comissao Comissao
db = 'comissao.txt'

def cadastraComissao(comissao):
    if consultarComissaoFuncionario(comissao['codigoComissao'],comissao['codigoFuncionario'], comissao['ano'], comissao['mes']):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s\n' % (comissao['codigoComissao'],comissao['codigoFuncionario'], comissao['ano'], comissao['mes'], comissao['valor'])))
    conexao.close()
    return True


def deletaComissaoFuncionario(codigoFuncionario,ano,mes)
	try
		f = open(db,"r")
		lines = f.readlines()
		f.close()
	
		f = open(db,"w")
		for linha in linhas:
			codigoFuncionario, ano, mes = linha.split('|')
			if codigoFuncionario != codigoFuncionario:
				f.write(linha)
		f.close()
		return True
	except:
		return False

def consultarComissaoFuncionario(codigoFuncionario,ano,mes)
    try:
        linhas = open(db,'r').read()
		f = open(db,"r")
		linhas = f.readlines()
		
		for linha in linhas:
			codigoFuncionario,ano,mes = linha.split('|')
			if cadastraComissao == codigo
				return True
		
		f.close()
		
		return False
        
    except:
        return False


serv = SOAPServer(("localhost", 8012))

serv.registerFunction(cadastraComissao)
serv.registerFunction(deletaComissaoFuncionario)
serv.registerFunction(consultarComissaoFuncionario)
serv.serve_forever()
