from SOAPpy import SOAPServer
from SOAPpy import SOAPProxy
db = 'cadastrarVenda.txt'

def cadastrarVenda(venda):
    conexao = open(db,'a')
    conexao.write("%s|%s\n" % (venda['codigoVenda'],venda['codigoCliente'], venda['codigoFuncionario'], venda['data'], venda['valortotal'], venda['codigoProduto'], venda['quantidade']))
    conexao.close()
    return True

def consultarVenda(codigoVenda):


serv = SOAPServer(("localhost", 8009))
serv.registerFunction(cadastrarVenda)
serv.registerFunction(consultarVenda)


serv.serve_forever()