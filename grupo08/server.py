#-*-encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy

db = 'funcionario.txt'

class ServicoVendaFake():
  def consultarVendaPorFuncionario(self, codigoFuncionario):
    if codigoFuncionario == '7':
      return [{
       'codigoVenda': 1,
       'codigoCliente': 1,
       'codigoFuncionario': 7,
       'data': '05/06/2015',
       'valor': 500
      }]
    else:
      return []


def cadastraFuncionario(funcionario):
 if consultaFuncionario(funcionario['codigo']):
    return False
 conexao = open(db,'a')
 conexao.write('%s|%s|%s|%s|%s\n' % (funcionario['codigo'],funcionario['nome'], funcionario ['endereco'], funcionario ['sexo'], funcionario ['datanascimento']))
 conexao.close()
 return True

def consultaFuncionario(codigoFuncionario):
  try:
       linhas = open(db,'r').read()
       f = open(db,"r")
       linhas = f.readlines()

       for linha in linhas:
           codigo, nome, endereco, sexo, datanascimento = linha.split('|')
           if codigoFuncionario == codigo:
              return True

       f.close()
       
       return False
  except:
    return False

def deletaFuncionario(codigoFuncionario):
  try:
    # servico = SOAPProxy("http://localhost:8009")
    servico = ServicoVendaFake()
    # import pdb; pdb.set_trace()
    vendas = servico.consultarVendaPorFuncionario(codigoFuncionario)
    if len(vendas) > 0:
      return False
    funcionarios = open(db, "r").readlines()

    existe = False

    for linha in funcionarios:
       codigo, nome, endereco, sexo, datanascimento = linha.split('|')
       if codigoFuncionario == codigo:
              existe = True

    if existe:
       
       f = open(db, "r")
       linhas = f.readlines()
       f.close()

       f = open(db, "w")
       for linha in linhas:
              codigo, nome, endereco, sexo, datanascimento = linha.split ('|')
              if codigo != codigoFuncionario:
                    f.write(linha)
       f.close()

       return True
  except:
    return False    

       

def listaFuncionario():
  try:
    f = open(db, "r")
    linhas = f.readlines()
    return linhas
  except:
    return False

serv = SOAPServer(("localhost", 8008))

serv.registerFunction(consultaFuncionario)
serv.registerFunction(cadastraFuncionario)
serv.registerFunction(listaFuncionario)
serv.registerFunction(deletaFuncionario)

serv.serve_forever() 