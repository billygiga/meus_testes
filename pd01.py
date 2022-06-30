import pandas as pd
import numpy as np
import random

dados = {
    'Funcionarios':['maria','joao','cleber','tereza','kaio','rodrigo','pedro','kaleb','lidia','marina'],
    'Ano_admissao':[2020,2022,2010,2011,2000,2013,2001,1990,2022,2022],
    'Salario':[2.300,1.500,4.350,6.400,1.700,3.200,4.300,2.100,4.800,2.150],
    'Hora_extra':random.sample(range(5,20),10),
    'Setor':['tecnico','zeladoria','supervisao','gerente',
             'estoque','analista','progetista','officeboy','gestor','promotor']
}

df = pd.DataFrame(dados)

for salario in dados['Salario']:
    diaria = salario/20
    for extra in dados['Hora_extra']:
        total = diaria * extra
        df['Salario_liquido'] = total + df['Salario']

print(df.loc[(df['Salario']) < 2.500])
print()
print(df.loc[(df['Ano_admissao']) == 2022])

