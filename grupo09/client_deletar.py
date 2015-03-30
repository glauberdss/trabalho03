from SOAPpy import SOAPProxy
service = SOAPProxy("http://localhost:8009")

sale= raw_input('Codigo da Venda: ')
if service.deletarVenda(sale):
	print 'Deletada com sucesso'
else:
	print 'Venda nao cadastrada'
