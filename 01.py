import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gulugu777",
    database="mercado_database"
)

ferramenta = conexao.cursor()

ferramenta.execute("SELECT * FROM produtos")

resultado = ferramenta.fetchall()

def seletor():
    menu = input ('Escolha a função desejada: ')
    
    if menu not in opcoes:
        print ('Escolha 1, 2 ou 3')
        return
    
    if menu == '1':
        print ('sla porra')
    
    elif menu == '2':
        print ('sla dnv')
            
    elif menu == '3':
        print ('=== Menu ===')

def infos():
    visualizar = input ('Visualizar produtos? ').lower()
    
    if visualizar == 'nao' or visualizar == 'não':
        menu()
       
    elif visualizar == 'sim':
        print (resultado)

def novo_produto():
    nome = input ('Adicione o nome do produto: ')
    preco = float(input('Digite o preço: '))
    quantidade = int(input('Digite a quantidade em estoque: '))
                
    ferramenta.execute ((f"Insert into produtos(nome, preco, quantidade) values ('{nome}', {preco}, {quantidade})"))
    conexao.commit()
    ferramenta.execute ('select * from produtos')
    resultado = ferramenta.fetchall()

def excluir_produto():
    nome = input ('Insira o nome do produto: ')

    ferramenta.execute ((f"delete from produtos where nome = '{nome}'"))
    conexao.commit()
    ferramenta.execute ('select * from produtos')
    resultado = ferramenta.fetchall()

opcoes = ['1', '2', '3']
opcoes2 = ['sim', 'não', 'nao']

while True:

    print ('1- Menu')
    print ('2 - Registro de compras')
    print ('3 - Mercadorias')

    menu = seletor()

    visualizar = infos()

    adicionar = input ('Deseja adicionar um produto? ')

    if adicionar == 'sim':
        novo_produto()

    deletar = input ('Deseja excluir um produto? ')

    if deletar == 'sim':
        excluir_produto()