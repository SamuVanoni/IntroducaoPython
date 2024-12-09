def adicionar_contato(contatos, nome, telefone, email):
    contato = {"Nome": nome, "Telefone": telefone, "E-mail": email, "Favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionado(a) com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["Favorito"] else " "
        print(f"{indice}. {contato["Nome"]}, Telefone: {contato["Telefone"]}, E-mail: {contato["E-mail"]}, Favorito: [{status}]")
    return

def atualizar_nome_contato(contatos, indice_contato, novo_nome):
    if indice_contato - 1 >= 0 and indice_contato - 1 < len(contatos):
        contatos[indice_contato - 1]["Nome"] = novo_nome
        print(f"Nome {indice_contato} atualizado(a) para {novo_nome}!")
    else:
        print("Índice do contato inválido.")
    return

def marcar_desmarcar_favorito(contatos, indice_contato):
    if contatos[indice_contato - 1]["Favorito"] == True:
        contatos[indice_contato - 1]["Favorito"] = False
        print(f"Contato {indice_contato} foi desmarcado(a) como favorito!")
    else:
        contatos[indice_contato - 1]["Favorito"] = True
        print(f"Contato {indice_contato} foi marcado(a) como favorito!")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de contatos favoritados:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["Favorito"]:
            print(f"{indice}. {contato["Nome"]}, Telefone: {contato["Telefone"]}, E-mail: {contato["E-mail"]}, Favorito: [✓]")
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

    elif escolha == 2:
        ver_contatos(contatos)
    
    elif escolha == 3:
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que você deseja atualizar: "))
        novo_nome = input("Digite o novo nome do contato: ")
        atualizar_nome_contato(contatos, indice_contato, novo_nome)

    elif escolha == 4:
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que você deseja marcar/desmarcar de favorito: "))
        marcar_desmarcar_favorito(contatos, indice_contato)

    elif escolha == 5:
        ver_contatos_favoritos(contatos)

    elif escolha == 7:
        break

print("Programa finalizado!")