from SOAPpy import SOAPProxy

service = SOAPProxy("http://localhost:8009")

codigo_venda = raw_input('Codigo Venda: ')
codigo_cliente = raw_input('Codigo Cliente: ')
codigo_funcionario = raw_input('codigo Funcionario: ')
data = raw_input('Data: ')
valor_total = raw_input('Valor Total: ')
codigo_produto = raw_input('Codigo Produto: ')
quantidade = raw_input('Quantidade: ')

sale = {'codigo_venda':codigo_venda,'codigo_cliente':codigo_cliente,'codigo_funcionario':codigo_funcionario,'data' :data, 'valor_total' :valor_total, 'codigo_produto':codigo_produto, 'quantidade' :quantidade}

if service.cadastrarVenda(sale):
	print 'Cadastrado com sucesso'
else:
		print 'Nao foi possivel cadastrar a venda. Verifique se o codigo de venda ja nao existe.'