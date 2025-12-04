import time

# -------------------------------------------
# CABEÇALHO DO SISTEMA
# -------------------------------------------
def cabecalho(titulo):
    print("=" * 40)
    print(f"{titulo.center(40)}")
    print("=" * 40)

# -------------------------------------------
# LOGIN
# -------------------------------------------
def login():
    senha_correta = "adm"
    tentativas = 0

    cabecalho("LOGIN DO SISTEMA")

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print("Acesso autorizado!")
            print("\n" * 20)
            return True
        else:
            tentativas += 1
            print(f"Senha incorreta! Tentativa {tentativas}/3\n")

    print("Número máximo de tentativas atingido. Encerrando...")
    return False

# -------------------------------------------
# BARRA DE VERIFICAÇÃO
# -------------------------------------------
def barra_progresso(texto):
    print(f"{texto}\n")
    barra = 10
    for i in range(1, barra + 1):
        progresso = "#" * i + "-" * (barra - i)
        porcentagem = i * 10
        print(f"[{progresso}] {porcentagem}%")
        time.sleep(0.2)
    print("\n" * 20)

# -------------------------------------------
# SISTEMA DE VENDAS
# -------------------------------------------
def sistema_vendas():
    produtos = {
        "1": {"nome": "Caderno",  "preço": 12.99},
        "2": {"nome": "Lapis", "preço": 1.25},
        "3": {"nome": "Borracha", "preço": 2.50},
        "4": {"nome": "Caneta", "preço": 3.50}
    }

    carrinho = {}
    total_compra = 0

    while True:
        cabecalho("MERCADORIAS DISPONÍVEIS")
        for cod, info in produtos.items():
            print(f"{cod} - {info['nome']}  R${info['preço']}")

        print("\n0 - Finalizar compra")
        escolha = input("\nEscolha um produto: ")

        if escolha == "0":
            break

        if escolha in produtos:
            qtd = int(input(f"Quantos '{produtos[escolha]['nome']}' deseja? "))

            nome_produto = produtos[escolha]['nome']
            preco_produto = produtos[escolha]['preço']

            carrinho[nome_produto] = carrinho.get(nome_produto, 0) + qtd
            total_compra += preco_produto * qtd
            
            print("\nItem adicionado!")
            print(f"\nTotal parcial: R${total_compra:.2f}")
            time.sleep(0.7)

        else:
            print("Produto inválido!")
            time.sleep(1)

    return carrinho, total_compra, produtos

# -------------------------------------------
# FINALIZAÇÃO
# -------------------------------------------
def finalizar(carrinho, total_compra, produtos):
    cabecalho("RESUMO FINAL DA COMPRA")

    for item, qtd in carrinho.items():
        # acha o preço correto baseado no dicionário
        preco_item = next(prod["preço"] for prod in produtos.values() if prod["nome"] == item)
        print(f"{item} x{qtd} = R${preco_item * qtd:.2f}")

    print(f"\nSubtotal: R${total_compra:.2f}")

    # Desconto
    if total_compra > 100:
        desconto = total_compra * 0.10
        total_compra -= desconto
        print(f"Desconto aplicado: -R${desconto:.2f}")

    print(f"\nTOTAL A PAGAR: R${total_compra:.2f}")
    print("\nObrigado por comprar com a gente!")

    input("\nPressione ENTER para encerrar...")

# -------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------
if login():
    cabecalho("MENU PRINCIPAL")
    print("1 - Comprar produtos")
    print("2 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        barra_progresso("Verificando estoque...")
        carrinho, total, produtos = sistema_vendas()
        finalizar(carrinho, total, produtos)
    else:
        print("Programa encerrado.")
