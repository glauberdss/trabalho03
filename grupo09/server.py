#-*-encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer
from SOAPpy import SOAPProxy
db = 'cadastrarVenda.txt'

def cadastrarVenda(venda):
  if consultarVenda(venda['codigo_venda']):
    return False
  conexao = open(db,'a')
  conexao.write("%s|%s|%s|%s|%s|%s|%s\n" % (venda['codigo_venda'],venda['codigo_cliente'], venda['codigo_funcionario'], venda['data'], venda['valor_total'], venda['codigo_produto'], venda['quantidade']))
  conexao.close()
  return True

def consultarVenda(codigo_venda):
  try:
    lines = open(db,'r').read()
  except:
    return False
  retorno = 'Venda nao encontrada'
  for line in lines.split('\n'):
    venda = line.split('|')
    if (venda[0] == codigo_venda):
      retorno  = 'Venda '+venda[0]+' | Funcionario '+ venda[2]+' | Data '+venda[3]+' | Valor '+venda[4]+' | Produto '+venda[5]+' | Quantidade '+venda[6]
      return retorno

def deletarVenda(codigo_venda):
  service = SOAPProxy("http://localhost:8009")
  try:
    lines = open(db, "r").readlines()
    existe = False
    for line in lines:
      codigo_venda, codigo_cliente, codigo_funcionario, data, valor_total, codigo_produto, quantidade = line.split('|')
      if codigo_venda == codigo_venda:
        existe = True
    if existe:       
      v = open(db, "r")
      lines = v.readlines()
      v.close()

      v = open(db, "w")
      for line in lines:
        codigo_venda, codigo_cliente, codigo_funcionario, data, valor_total, codigo_produto, quantidade = line.split('|')
        if codigo_venda != codigo_venda:
          v.write(line)
      v.close()
      return True
  except:
    return False    

#método retornando 0 para sem vendas e 1 para com vendas
def verificaSeExisteVendaParaFuncionario(codigoFuncionario):
  try:
    linhas = open(db,'r').read()
    f = open(db,"r")
    linhas = f.readlines()
    for linha in linhas:
      codigo_venda,codigo_cliente,codigo_funcionario,data,valor_total,codigo_produto,quantidade = linha.split('|')
      if codigoFuncionario == codigo_funcionario:
        return True
    f.close()
    return False
  except:
    return False
    
serv = SOAPServer(("localhost", 8009))
serv.registerFunction(cadastrarVenda)
serv.registerFunction(consultarVenda)
serv.registerFunction(deletarVenda)
serv.registerFunction(verificaSeExisteVendaParaFuncionario)

serv.serve_forever()