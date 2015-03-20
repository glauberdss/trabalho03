#!/usr/bin/env python


from SOAPpy import SOAPProxy

servico = SOAPProxy("http://localhost:8008")

funcionario = servico.listaFuncionario()
print funcionario
