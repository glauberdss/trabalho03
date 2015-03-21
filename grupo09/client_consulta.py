from SOAPpy import SOAPProxy

service = SOAPProxy("http://localhost:8009")

print 'Selecione o codigo de :'
code = raw_input('codigo da Venda: ')
print service.consulte_sale(code)
