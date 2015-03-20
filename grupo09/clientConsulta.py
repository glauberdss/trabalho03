from SOAPpy import SOAPProxy

service = SOAPProxy("http://localhost:8009")

print 'Selecione o codigo de Consulta:'
consultacodigo = raw_input('codigo: ')
print service.consultarVenda(consultacodigo)
