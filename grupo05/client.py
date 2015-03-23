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



retorno = servico.listarFornecedor()
print retorno
