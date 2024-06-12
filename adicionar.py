import csv

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    novo_contato = {"nome": nome, "telefone": telefone, "email": email}

    adicionar_contato_arquivo(novo_contato)
    print("Contato adicionado com sucesso!")

def adicionar_contato_arquivo(contato):
    with open("contatos.csv", mode="a", newline="") as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "telefone", "email"])
        escritor_csv.writerow(contato)