from SOAPpy import SOAPProxy

# conectando diretamente
from os import fork

servico = SOAPProxy("http://localhost:8010")

print'Cadastrando Conta a Pagar'

codigoContaApagar =raw_input('Codigo da Conta a Pagar: ')
codigoCompra =raw_input('Codigo da Compra: ')
dataVencimento =raw_input('Data de Vencimento: ')
dataPagamento =raw_input('Data de Pagamento: ')
status =raw_input('Status: ')

ContaApagar ={'codigoContaApagar':codigoContaApagar,'codigoCompra':codigoCompra,'dataVencimento':dataVencimento,'dataPagamento':dataPagamento,'status':status}

if servico.cadastrarContaApagar(ContaApagar):
    print'Conta a Pagar cadastrada com sucesso'
"""

print'Consultar Conta a Pagar'
codigo =raw_input('Codigo da Conta a Pagar: ')
retorno = servico.consultarContaApagar(codigo)

if retorno is True:
    print 'Conta a Pagar existe na Base'
else:
    print'Conta a Pagar nao foi encontrado'


print 'Deletando Conta a Pagar'
codigo =raw_input('Codigo da Conta a Pagar: ')

if servico.deletarContaApagar(codigo) is True:
    print 'Conta a Pagar deletada com sucesso!'
else:
    print 'Conta a Pagar nao foi excluida'
"""
