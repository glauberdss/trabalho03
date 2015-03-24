from SOAPpy import SOAPProxy

# conectando diretamente
from os import fork

servico = SOAPProxy("http://localhost:8007")

print'Cadastrando Compra'
codigoCompra =raw_input('Codigo da Compra: ')
codigoProduto =raw_input('Codigo do Produto: ')
quantidade =raw_input('Quantidade: ')
data =raw_input('Data: ')
valortotal =raw_input('Valor Total: ')
codigoFornecedor =raw_input('Codigo do Fornecedor: ')

compra ={'codigoCompra':codigoCompra,'codigoProduto':codigoProduto,'quantidade':quantidade,'data':data,'valortotal':valortotal,'codigoFornecedor':codigoFornecedor}

if servico.cadastrarCompra(compra):
	print'Compra cadastrada com sucesso'


print'Consultar Compra'
codigo =raw_input('Codigo da Compra: ')
retorno = servico.consultarCompra(codigo)
if retorno is True:
    print 'Compra existe na Base'
else:
    print'Compra nao foi encontrado'


print 'Deletando Compra'
codigo =raw_input('Codigo da Compra: ')

if servico.deletarCompra(codigo) is True:
    print 'Compra deletada com sucesso!'
else:
    print 'Compra nao foi excluida'
