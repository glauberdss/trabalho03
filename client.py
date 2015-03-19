#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8080")


usuario = raw_input('Usuario: ')
senha = raw_input('Senha: ')

user ={'usuario':usuario,'senha':senha}

#if servico.login(usuario,senha):
if servico.login(user):
    print 'Login efetuado com sucesso'
else:
    print 'O usuario nao existe ainda, cadastrando'
    servico.registra(user)
