# Challenge 01 - Contact Book

def add_contact(schedule, name, telephone, email):
    contact = {"name": name, "telephone": telephone, "email": email, "favorite": False}
    schedule.append(contact)
    print(f"Contato {name} foi adicionado com sucessso!")
    return

def view_contacts(schedule):
    print("\nAgenda De Contatos")
    for index, contact in enumerate(schedule, start=1):
        favorite = "*" if contact["favorite"] else ""
        name = contact["name"]
        telephone = contact["telephone"]
        email = contact["email"]
        print(f"{index}. [{favorite}] {name}, {telephone}, {email}")
    
    if len(schedule) == 0:
        print("\nOps! Sua lista de contatos ainda está vazia.")
    return

def update_contact(schedule, index_contact, new_name, new_telephone, new_email):
    adjusted_contact_index = int(index_contact) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(schedule):
        schedule[adjusted_contact_index]["name"] = new_name
        schedule[adjusted_contact_index]["telephone"] = new_telephone
        schedule[adjusted_contact_index]["email"] = new_email
        print(f"Contato {index_contact} atualizado para {new_name}, {new_telephone}, {new_email}")
    else:
        print("Índice de contato inválido")
    return

def favorite_contact(schedule, index_contact):
    adjusted_contact_index = int(index_contact) - 1
    schedule[adjusted_contact_index]["favorite"] = True
    print(f"Contato {index_contact} marcado como favorito!")
    return

def unfavorite_contact(schedule, index_contact):
    adjusted_contact_index = int(index_contact) - 1
    schedule[adjusted_contact_index]["favorite"] = False
    print(f"O contato {index_contact} foi removido dos favoritos.")
    return

def view_favorite_contacts(schedule):
    print("\nSeus contatos favoritados")
    for index, contact in enumerate(schedule, start=1):
        if contact["favorite"]:
            name = contact["name"]
            telephone = contact["telephone"]
            email = contact["email"]
            print(f"{index}. {name} - {telephone} - {email}")
    return

def delete_contact(schedule, index_contact):
    adjusted_contact_index = int(index_contact) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(schedule):
        contact = schedule[adjusted_contact_index]
        schedule.remove(contact)
        print(f"Contato {index_contact} deletado com sucesso!")
    else: 
        print("Indice do contato inválido.")
    return


schedule = []

while True:
    print("\nBem-vindo(a) ao Menu da sua Agenda de Contatos!")
    print("\n1. Adicionar contato:")
    print("2. Ver contatos:")
    print("3. Editar contato:")
    print("4. Favoritar contato:")
    print("5. Remover contato dos favoritos:")
    print("6. Visualizar contatos favoritados:")
    print("7. Apagar contato:")
    print("8. Sair:")

    choice = input("\nDigite sua escolha: ")

    if choice == "1":
        name = input("Insira o nome de seu contato: ")
        telephone = input("Insira o telefone de seu contato: ")
        email = input("Insira o e-mail de seu contato: ")
        add_contact(schedule, name, telephone, email)
    elif choice == "2":
        view_contacts(schedule)
    elif choice == "3":
        view_contacts(schedule)
        index_contact = input("Digite o número do contato que deseja atualizar: ")
        new_name = input("Digite o novo nome de seu contato: ")
        new_telephone = input("Digite o novo número de telefone de seu contato: ")
        new_email = input("Digite o novo e-mail de seu contato: ")
        update_contact(schedule, index_contact, new_name, new_telephone, new_email)
    elif choice == "4":
        view_contacts(schedule)
        index_contact = input("Digite o número do contato que deseja favoritar: ")
        favorite_contact(schedule, index_contact)
    elif choice == "5":
        view_contacts(schedule)
        index_contact = input("Digite o número do contato que deseja remover dos favoritos: ")
        unfavorite_contact(schedule, index_contact)
    elif choice == "6":
        view_favorite_contacts(schedule)
    elif choice == "7":
        view_contacts(schedule)
        index_contact = int(input("Digite o número do contato que deseja remover de sua agenda: "))
        delete_contact(schedule, index_contact)
    elif choice == "8":
        break
