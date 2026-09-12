opcoes = ['1', '2', '3']
opcoes2 = ['sim', 'não', 'nao']
produto = ['arroz', 'feijão']

while True:

    print ('1- Menu')
    print ('2 - Registro de compras')
    print ('3 - Mercadorias')

    menu = input ('Escolha a função desejada: ')

    if menu not in opcoes:
        print ('Escolha 1, 2 ou 3')
        continue

    if menu == '1':
        print ('sla porra')

    elif menu == '2':
        print ('sla dnv')
        
    elif menu == '3':
        print ('=== Menu ===')

        visualizar = input ('Visualizar produtos? ').lower()
            
        if visualizar == 'sim':
                for produtos in produto:
                    print (produtos)

        elif visualizar == 'nao' or visualizar == 'não':
            continue

        novo_produto = input ('Deseja adicionar um produto? ')

        if novo_produto == 'sim':
            novo_produto = input ('Adicione o produto: ')
            produto.append (novo_produto)

        elif novo_produto == 'nao' or novo_produto == 'não':
            continue