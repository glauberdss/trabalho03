from SOAPpy import SOAPServer
from SOAPpy import SOAPProxy

db = 'ContaApagar.txt'

def cadastrarContaApagar(ContaApagar):
        if consultarContaApagar(ContaApagar['codigoContaApagar']):
            return False
            conexao = open(db,'a')
            conexao.write('%s|%s|%s|%s|%s|%s\n' % (ContaApagar['codigoContaApagar'],ContaApagar['codigoCompra'],     ContaApagar['dataVencimento'], ContaApagar['dataPagamento'], ContaApagar['status']))
            conexao.close()
            return True

def deletarContaApagar(codigoContaApagar):
    try:
        f = open(db,"r")
        linhas = f.readlines()
        f.close()
        f = open(db,"w")
    
        for linha in linhas:
            codigoContaApagar_, codigoCompra, dataVencimento, dataPagamento, status = linha.split('|')
        if codigoContaApagar != codigoContaApagar_:
            f.write(linha)
            f.close()
            return True

    except:
        return False

def consultarContaApagar(codigoContaApagar):
    try:
        linhas = open(db,'r').read()
        f = open(db,"r")
        linhas = f.readlines()

        for linha in linhas:
            codigoContaApagar_, codigoCompra, dataVencimento, dataPagamento, status = linha.split('|')
        if codigoContaApagar_ == codigoContaApagar:
            f.close()
            return True
        f.close()
        return False

    except:
        return False

def listarContaApagar():
    try:
        linhas = open(db,'r').read()
        f = open(db,"r")
        linhas = f.readlines()
        return linhas

    except:
        return False


serv = SOAPServer(("localhost", 8010))
serv.registerFunction(consultarContaApagar)
serv.registerFunction(cadastrarContaApagar)
serv.registerFunction(deletarContaApagar)
    
serv.serve_forever()
