import csv

def atualizar_contato():
    nome = input("Digite o nome do contato que deseja atualizar: ")
    telefone_novo = input("Digite o novo telefone (ou deixe em branco para manter o atual): ")
    email_novo = input("Digite o novo email (ou deixe em branco para manter o atual): ")

    contatos_atualizados = []

    with open("contatos.csv", mode="r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for contato in leitor_csv:
            if contato["nome"] == nome:
                if telefone_novo:
                    contato["telefone"] = telefone_novo
                if email_novo:
                    contato["email"] = email_novo
            contatos_atualizados.append(contato)

    with open("contatos.csv", mode="w", newline="") as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "telefone", "email"])
        escritor_csv.writeheader()
        escritor_csv.writerows(contatos_atualizados)

    print("Contato atualizado com sucesso!")