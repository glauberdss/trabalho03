#-*-encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer

from SOAPpy import SOAPProxy

db = 'funcionario.txt'

def cadastraFuncionario(funcionario):
 if consultaFuncionario(funcionario['codigo']):
    return False
 conexao = open(db,'a')
 conexao.write('%s|%s|%s|%s|%s\n' % (funcionario['codigo'],funcionario['nome'], funcionario ['endereco'], funcionario ['sexo'], funcionario ['datanascimento']))
 conexao.close()
 return True

def consultaFuncionario(codigoFuncionario):
  try:
    linhas = open(db, 'r').read()
    f = open(db, "r")
    linhas = f.readlines()

    for linha in linhas:
      codigo, nome, endereco, sexo, datanascimento = linha.split('|')
      if codigoFuncionario == codigo:
        return True

    f.close()
    return False

  except:
    return False

  def listaFuncionario():
    try:
      linhas = open(db, 'r'). read()
      f = open(db, "r")
      linhas = f.readlines()
      return linhas
    except:
      return False

  serv = SOAPServer(("localhost", 8008))

  serv.registerFunction(consultaFuncionario)
  serv.registerFunction(cadastraFuncionario)
  serv.registerFunction(listaFuncionario)

  serv.serve_forever() 