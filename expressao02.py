import re

reg = re.compile('[0-9]{2}[/][0-9]{2}[/][0-9]{4}')

data = input('digite uma data valida :')

if reg.findall(data):
    print(data)
else:
    print('data invalida')