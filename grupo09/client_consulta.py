from SOAPpy import SOAPProxy

service = SOAPProxy("http://localhost:8009")
code = raw_input('codigo da Venda: ')

if service.consultarVenda(code):
  print service.consultarVenda(code)
else:
  print 'nao encontrado'
