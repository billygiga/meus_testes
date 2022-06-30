import sqlite3

conn = sqlite3.connect('meu_bd.db')
cursor = conn.cursor()


def add():
    p_nome = input('Nome: ')
    p_idade = input('Idade: ')
    p_cpf = input('CPF: ')

    cursor.execute('''INSERT INTO dados01 (nome, idade, cpf) VALUES (?,?,?)''',(p_nome, p_idade, p_cpf))

    conn.commit()

    print('cadastrado com sucesso.')


cursor.execute("""
SELECT * FROM dados01;
""")

for linha in cursor.fetchall():
    print(f'nome:{linha[1]}\nidade:{linha[2]}\ncpf:{linha[3]}')
    print('='*30)

# desconectando...
conn.close()
