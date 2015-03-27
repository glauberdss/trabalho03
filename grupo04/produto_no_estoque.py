#-*- encoding: iso-8859-1 -*-
import json

class DB(list):

    def __init__(self, *args, **kwargs):
        super(DB, self).__init__(*args, **kwargs)
        self.extend(json.load(open('DB', 'rb')))

    def adicionar(self, item):
        self.append(item)
        json.dump(self, open('DB', 'wb'))
        return self

    def procurar(self, match):
        return filter(match, self)


class ProdutoNoEstoque(dict):

    def salvar(self):
        DB().adicionar(self)
        return True

    @classmethod
    def verificar_quantidade(cls, cod_produto, cod_estoque):
        resultado = DB().procurar(lambda item: ([cod_produto, cod_estoque] ==
            [item['codigo_produto'], item['codigo_estoque']])
        )
        return resultado[0]['quantidade'] if resultado else 0
