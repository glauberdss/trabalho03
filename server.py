#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer
db = 'usuarios.txt'


def login(user):
    try:
        linhas = open(db,'r').read()
    except:
        return False

    for linha in linhas.split('\n'):

        if linha == '':
           break
        user1,passwd = linha.split('|')
        if user['usuario'] == user1 and user['senha'] == passwd:
            return True
    return False


def registra(user):
    if login(user):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s\n' % (user['usuario'],user['senha']))
    conexao.close()
    return True

serv = SOAPServer(("localhost", 8080))

serv.registerFunction(login)
serv.registerFunction(registra)
serv.serve_forever()
