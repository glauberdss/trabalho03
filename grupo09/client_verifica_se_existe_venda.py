from SOAPpy import SOAPProxy
service = SOAPProxy("http://localhost:8009")
code = raw_input('codigo do Funcionario: ')
print service.verificaSeExisteVendaParaFuncionario(code)

