import re


reg = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')

cpf = input('cpf :')
if reg.findall(cpf):
    print(reg.findall(cpf))
else:
    print('cpf invalido')