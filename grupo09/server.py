from SOAPpy import SOAPServer
from SOAPpy import SOAPProxy
db = 'cadastrarVenda.txt'
def cadastrarVenda(venda):
    conexao = open(db,'a')
    conexao.write("%s|%s\n" % (venda['codigoVenda'],venda['codigoCliente'], venda['codigoFuncionario'], venda['data'], venda['valortotal'], venda['codigoProduto'], venda['quantidade']))
    conexao.close()
    return True

def consultarVenda(codigoVenda):
    try:
        linhas = open(db,'r').read()
    except:
        return False
    retorno = 'V encontrado'
    for linha in linhas.split('\n'):
        venda = linha.split('|')
        if (venda[0] == codigoVenda):
          retorno  = ' Codigo Venda '+venda[0]+' Codigo Funcionario '+ venda[2]+' Data '+venda[3]+' Valor '+venda[4]+' Codigo Produto '+venda[5]+' Quantidade '+venda[6]
          return retorno
serv = SOAPServer(("localhost", 8009))
serv.registerFunction(cadastrarVenda)
serv.registerFunction(consultarVenda)
serv.registerFunction(DeletarVenda
serv.serve_forever()