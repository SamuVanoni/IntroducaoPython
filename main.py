def adicionar_contato(contatos, nome, telefone, email):
    contato = {"Nome": nome, "Telefone": telefone, "E-mail": email, "Favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionado(a) com sucesso!")
    return

contatos = []
while True:
    print("\nMenu do Gerenciador de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver contatos marcados como favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome = input("Digite o nome do contato que deseja adicionar: ")
        telefone = input("Digite o telefone do contato que deseja adicionar: ")
        email = input("Digite o e-mail do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome, telefone, email)
        print(contatos)

    elif escolha == 7:
        break

print("Programa finalizado!")