class Veiculo:
    __slots__ = ['fabricante', 'ano', 'chassi']

    def __init__(self,fabricante,ano,chassi):
        self.fabricante = fabricante
        self.ano = ano
        self.chassi = chassi


class Carro(Veiculo):
    def __init__(self,fabricante,ano,chassi,marca,cor):
        super().__init__(fabricante,ano,chassi)
        self._marca = marca
        self._cor = cor

    def __repr__(self):
        return f'fabricante: {self.fabricante} \nano:{self.ano} ' \
               f'\nchassi:{self.chassi} \nmarca:{self.marca} \ncor:{self.cor}'

    @property
    def marca(self):
        return self._marca

    @property
    def cor(self):
        return self._cor


class Moto(Veiculo):
    def __init__(self,fabricante,ano,chassi,marca,cor):
        super().__init__(fabricante, ano, chassi)
        self._marca = marca
        self._cor = cor

    def __repr__(self):
        return f'fabricante: {self.fabricante} \nano:{self.ano} ' \
               f'\nchassi:{self.chassi} \nmarca:{self.marca} \ncor:{self.cor}'

    @property
    def marca(self):
        return self._marca

    @property
    def cor(self):
        return self._cor


if __name__ == '__main__':
    c1 = Carro('ford',2020,345345345345,'ford ka','azul')
    print(c1)
    print()
    m1 = Moto('honda',2012,34543454345,'start','preta')
    print(m1)
    
