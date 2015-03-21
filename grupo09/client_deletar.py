from SOAPpy import SOAPProxy
service = SOAPProxy("http://localhost:8009")

sale= raw_input('Codigo da Venda ')
if service.delete_sale(sale):
	print 'Deletada com sucesso'
else:
	print 'Venda nao cadastrada'
