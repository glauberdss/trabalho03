#!/usr/bin/env python

from SOAPpy import SOAPProxy

# conectando diretamente
servico = SOAPProxy("http://localhost:8082")

fabricantes = servico.listaFabricantes()

print fabricantes
