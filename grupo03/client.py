from SOAPpy import SOAPProxy

# conectando diretamente
from os import fork

servico = SOAPProxy("http://localhost:8003")

print'Cadastrando Produto'
codigo =raw_input('Codigo: ')
descricao =raw_input('Descricao: ')
preco =raw_input('Preco: ')
codigoFabricante =raw_input('Fabricante: ')

produto ={'codigo':codigo,'descricao':descricao,'preco':preco, 'codigoFabricante':codigoFabricante}

if servico.cadastrarProduto(produto):
	print'Produto cadastrado com sucesso!'


print'Listando todos os produtos'
retorno = servico.listarProduto()
print retorno


#validando
print'Consultando Produto'
retorno = servico.consultaProduto(1)
print retorno

print 'Deletando Produto'
codigo =raw_input('Codigo do Produto: ')

if servico.deletarProduto(codigo) is True:
    print 'Produto deletado com sucesso!'
else:
    print 'Produto esta em estoque e nao pode ser excluido'
