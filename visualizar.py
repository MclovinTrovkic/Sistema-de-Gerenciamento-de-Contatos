import csv

def visualizar_contatos():
    print("Visualizando todos os contatos:")
    print("Nome - Telefone - Email")
    print("------------------------------")
    
    with open("contatos.csv", mode="r") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for contato in leitor_csv:
            print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")