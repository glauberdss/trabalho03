#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8012")

codigoFun = raw_input('Codigo do Funcionario: ')
ano = raw_input('Ano: ')
mes = raw_input('Mes: ')

print servico.calcularComissao(codigoFun,ano,mes)

