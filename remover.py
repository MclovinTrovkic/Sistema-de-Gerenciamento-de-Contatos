import csv

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")

    contatos_restantes = []

    with open("contatos.csv", mode="r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for contato in leitor_csv:
            if contato["nome"] != nome:
                contatos_restantes.append(contato)

    with open("contatos.csv", mode="w", newline="") as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "telefone", "email"])
        escritor_csv.writeheader()
        escritor_csv.writerows(contatos_restantes)

    print("Contato removido com sucesso!")