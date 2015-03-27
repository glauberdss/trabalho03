# -*- coding: utf-8 -*-

import json, time
from subprocess import Popen
from SOAPpy import SOAPProxy

def reset_db():
    json.dump([], open('DB', 'w'))
reset_db()

server_process = Popen(['python', 'server.py'])
time.sleep(1)

client = SOAPProxy("http://localhost:8004")

try:
    assert client.inserirProdutoEstoque(1, 1, 5)
    assert client.inserirProdutoEstoque(1, 2, 5) == False
    assert client.inserirProdutoEstoque(2, 1, 5) == False

    assert client.consultaProdutoEmEstoque(1, 1) == 5
    assert client.consultaProdutoEmEstoque(1, 2) == 0
    assert client.consultaProdutoEmEstoque(2, 1) == 0

    assert client.consultaEstoqueEmProdutoEstoque(1)
    assert client.consultaEstoqueEmProdutoEstoque(2) == False
    #assert client.pesquisaPrecoProdutoEstoque(1) == 45.5
except AssertionError, erro:
    print "\033[1m\033[91mtests failed!\033[0m"
    raise
else:
    print "\033[1m\033[92mall tests passed!\033[0m"
finally:
    server_process.kill()
    reset_db()
