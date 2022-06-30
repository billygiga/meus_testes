class Loja:
    def __init__(self,**produtos):
        self.produtos = dict(produtos)
        for k,v in produtos.items():
            print(f'produto:{k} valor:{v}')

    def total(self):
        self.valor = round(sum(self.produtos.values()), 2)
        return f'total dos produtos: R${self.valor}'

    def aplicar_desconto(self,per):
        self.valor = self.valor - per / 100 * self.valor
        print(f'valor com desconto de {per}% R${round(self.valor,2)}')


if __name__ == '__main__':
    cliente01 = Loja(mesa=45.88,cadeira=23.33,chapeu=12.45)
    print(cliente01.total())
    cliente01.aplicar_desconto(15)
    print('='*35)
    cliente02 = Loja(mochila=95.28, oculos=20.50, tenis=112.90)
    print(cliente02.total())
    cliente02.aplicar_desconto(25)








