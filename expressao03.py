import re
#\

reg = re.compile('[0-9]{2}-9[0-9]{4}-[0-9]{4}')

telefone = '85-98678-0709'

print(re.findall(r'[a-z]{2}','ola munDo 89',re.IGNORECASE))


