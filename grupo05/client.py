from SOAPpy import SOAPProxy

# conectando diretamente
from os import fork

servico = SOAPProxy("http://localhost:8005")

print'Cadastrando Fornecedor'
codigo =raw_input('Codigo: ')
nome =raw_input('Nome: ')
contato =raw_input('Contato: ')

fornecedor ={'codigo':codigo,'nome':nome,'contato':contato}

if servico.cadastraFornecedor(fornecedor):
	print'Fornecedor cadastrado com sucesso'


print'Listando todos os Fornecedores cadastrados'
retorno = servico.listarFornecedor()
print retorno


print'Consultando Fornecedor'
codigo =raw_input('Codigo do Fornecedor: ')
retorno = servico.consultaFornecedor(codigo)
print retorno
if retorno:
    print 'Fornecedor existe na Base'
else:
    print'Fornecedor nao foi encontrado'


print 'Deletando Fornecedor'
codigoDeletar =raw_input('Codigo do Fornecedor: ')

if servico.deletarFornecedor(codigoDeletar):
    print 'Fornecedor deletado com sucesso!'
else:
    print 'Fornecedor esta em estoque e nao pode ser excluido'
