# Dicionário de produtos
produtos = {}

# Carrinho de compras
carrinho = []

# Menu interativo
while True:
    print("----- Menu de Gerenciamento de Produtos -----")
    print("1. Incluir Produto")
    print("2. Alterar Produto")
    print("3. Comprar Produto")
    print("4. Consultar Produto")
    print("5. Finalizar Compra")
    print("6. Sair")
    opcao = input("Digite a opção desejada: ")

    # Incluir Produto
    if opcao == "1":
        codigo = input("Código do produto: ")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço do produto: "))
        produtos[codigo] = {"nome": nome, "quantidade": quantidade, "preco": preco} #para incluir valores dentro de dicionários, é necessário escrever o nome do dicionário, a chave que ele terá e a lista a qual será atribuído
    
    # Alterar Produto
    elif opcao == "2":
        codigo = input("Código do produto a ser alterado: ")
        if codigo in produtos:
            nome = input("Novo nome do produto: ")
            quantidade = int(input("Nova quantidade em estoque: "))
            preco = float(input("Novo preço do produto: "))
            produtos[codigo] = {"nome": nome, "quantidade": quantidade, "preco": preco}
        else:
            print("Produto não encontrado.")
    
    # Comprar Produto
    elif opcao == "3":
        codigo = input("Código do produto a ser comprado: ")
        if codigo in produtos:
            quantidade_a_comprar = int(input("Quantidade a ser comprada: "))
            if quantidade_a_comprar <= produtos[codigo]["quantidade"]:
                produtos[codigo]["quantidade"] -= quantidade_a_comprar
                carrinho.append({"codigo": codigo, "quantidade": quantidade_a_comprar})
                print("Produto adicionado ao carrinho.")
            else:
                print("Quantidade indisponível.")
        else:
            print("Produto não encontrado.")
    
    # Consultar Produto
    elif opcao == "4":
        codigo = input("Código do produto a ser consultado: ")
        if codigo in produtos:
            print(f"Nome: {produtos[codigo]['nome']}")
            print(f"Quantidade em estoque: {produtos[codigo]['quantidade']}")
            print(f"Preço: R$ {produtos[codigo]['preco']}")
        else:
            print("Produto não encontrado.")
    
    # Finalizar Compra
    elif opcao == "5":
        if len(carrinho) > 0:
            valor_total = 0
            for item in carrinho:
                valor_total += produtos[item["codigo"]]["preco"] * item["quantidade"]
            
            print("----- Resumo da Compra -----")
            for item in carrinho:
                print(f"{produtos[item['codigo']]['nome']} x{item['quantidade']}: R$ {produtos[item['codigo']]['preco'] * item['quantidade']}")
            print(f"Valor total: R$ {valor_total}")
            
            # Código para pagamento aqui
            forma_pagamento = input("Forma de pagamento (crédito/débito): ")
            if forma_pagamento == "credito":
                print("Compra realizada com cartão de crédito.")
            elif forma_pagamento == "debito":
                print("Compra realizada com cartão de débito.")
            else:
                print("Forma de pagamento inválida.")
            
            carrinho.clear()
        else:
            print("Carrinho vazio.")
    
    # Sair
    elif opcao == "6":
        print("Saindo do sistema.")
        break
    
    else:
        print("Opção inválida.")


