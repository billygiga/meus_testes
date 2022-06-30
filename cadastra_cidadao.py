import sys
import time


print('====CADASTRAR CIDADAO====')

dados = {}
pessoas = []

print('1) cadastrat')
print('2) excluir')
print('3) alterar')
print('4) exibir')
print('5) sair')

while True:
    opp = int(input('digite uma opcao :'))
    time.sleep(1)
    if opp == 1:
        dados['nome'] = str(input('digite o nome da pessoa :'))
        dados['idade'] = int(input('digite a idade da pessoa :'))
        dados['cidade'] = str(input('digite a cidade :'))
        op = str(input('quer cadastrar outra pessoa [S/N]? :'))
        pessoas.append(dados.copy())

        if op in 'Nn':
            continue
        time.sleep(1)
    if opp == 2:
        n = str(input('digite o nome da pessoa que quer excluir :'))
        for pessoa in pessoas:
            if pessoa['nome'] == n:
                pessoa.clear()

    if opp == 3:
        op = str(input('qual pessoa quer alterar? :'))
        time.sleep(1)
        for pessoa in pessoas:

            if pessoa['nome'] == op:
                da = str(input('qual dado que alterar? :'))
                time.sleep(1)
                if da == 'nome':
                    dados['nome'] = str(input('digite o nome da pessoa :'))
                    pessoas.append(dados.update())
                    break
                elif da == 'idade':
                    dados['idade'] = int(input('digite a idade da pessoa :'))
                    pessoas.append(dados.copy())
                    break
                elif da == 'cidade':
                    dados['cidade'] = str(input('digite a cidade :'))
                    pessoas.append(dados.copy())
                    break

    if opp == 4:
        if len(pessoas) > 0:
            for pessoa in pessoas:
                print(pessoa)
        else:
            print('nao ha usuarios cadastrados')

    if opp == 5:
       sys.exit()


