import adicionar
import visualizar
import atualizar
import remover

def main_menu():
    while True:
        print("Menu:")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Atualizar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar.adicionar_contato()
        elif opcao == "2":
            visualizar.visualizar_contatos()
        elif opcao == "3":
            atualizar.atualizar_contato()
        elif opcao == "4":
            remover.remover_contato()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")