class Cidadao:
    __slots__ = ['nome', 'idade']

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaFisica(Cidadao):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    def __repr__(self):
        return f'nome: {self.nome} \nidade: {self.idade} \ncpf: {self._cpf}'


class PessoaJuritica(Cidadao):
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self._cnpj = cnpj

    @property
    def cnpj(self):
        return self._cnpj

    def __repr__(self):
        return f'nome: {self.nome} \nidade: {self.idade} \ncpf: {self.cnpj}'


if __name__ == '__main__':
    pf = PessoaFisica('paulo', 23, 89876545463)
    print(pf)
    print()
    pj = PessoaJuritica('marilia', 33, 64640001746)
    print(pj)

