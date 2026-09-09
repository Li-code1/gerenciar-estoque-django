def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip()
    try:
        quantidade = int(input(f"Quantidade de {nome}: "))
        preco = float(input(f"Preço de {nome}: R$ "))
        estoque[nome] = {"quantidade": quantidade, "preco": preco}
        print(f"✅ Produto '{nome}' adicionado com sucesso!")
    except ValueError:
        print("❌ Erro: Quantidade e preço devem ser valores numéricos.")

def listar_produtos(estoque):
    if not estoque:
        print("\n📭 O estoque está vazio.")
        return

    print("\n--- Lista de Produtos (Ordem Alfabética) ---")
    # Ordenando as chaves (nomes) usando lambda
    produtos_ordenados = sorted(estoque.items(), key=lambda item: item[0].lower())
    
    for nome, dados in produtos_ordenados:
        print(f"Produto: {nome} | Qtd: {dados['quantidade']} | Preço: R$ {dados['preco']:.2f}")

def remover_produto(estoque):
    nome = input("Digite o nome do produto para remover: ").strip()
    if nome in estoque:
        del estoque[nome]
        print(f"🗑️ Produto '{nome}' removido!")
    else:
        print(f"⚠️ Erro: O produto '{nome}' não foi encontrado.")

def atualizar_quantidade(estoque):
    nome = input("Digite o nome do produto para atualizar: ").strip()
    if nome in estoque:
        try:
            nova_qtd = int(input(f"Nova quantidade para {nome}: "))
            estoque[nome]["quantidade"] = nova_qtd
            print(f"🔄 Quantidade de '{nome}' atualizada para {nova_qtd}.")
        except ValueError:
            print("❌ Erro: A quantidade deve ser um número inteiro.")
    else:
        print(f"⚠️ Erro: O produto '{nome}' não existe.")

def menu():
    estoque = {}
    
    while True:
        print("\n--- GERENCIADOR DE ESTOQUE ---")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Remover produto")
        print("4. Atualizar quantidade de produto")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            atualizar_quantidade(estoque)
        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("🚫 Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()