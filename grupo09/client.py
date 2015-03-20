from SOAPpy import SOAPProxy

service = SOAPProxy("http://localhost:8009")

codigoVenda = raw_input('Codigo Venda: ')
codigoCliente = raw_input('Codigo Cliente: ')
codigoFuncionario = raw_input('codigo Funcionario: ')
data = raw_input('Data: ')
valortotal = raw_input('Valor Total: ')
codigoProduto = raw_input('Codigo Produto: ')
quantidade = raw_input('Quantidade: ')

venda = {'codigoVenda':codigoVenda,'codigoCliente':codigoCliente,'codigoFuncionario':codigoFuncionario,'data' :data, 'valortotal' :valortotal, 'codigoProduto' :codigoProduto, 'quantidade' :quantidade}

if service.cadastrarVenda(venda):
	print 'Cadastrado com sucesso'
