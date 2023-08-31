from classes import *

Tarefas = []

def main():

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---MENU---")
            print("1 - ADICIONAR TAREFAS")
            print("2 - EXCLUIR TAREFAS")
            print("3 - LISTAR TAREFAS")
            print("0 - SAIR")


            print("Qual opção deseja?")
            menu = int(input(">> "))
            os.system("pause")

            match menu:
                case 1:

                    print("---ADICIONAR TAREFAS---")
                    print("INFORME SUA TAREFA")
                    descricao = input(">> ")
                    ToDoList.adicionar_tarefa(descricao)
                    print("TAREFA SALVA")
                    print("--------")
                
                case 2:

                    ToDoList.excluir_tarefa
                
                case 3:
                    print("LISTA DE TAREFAS")
                    ToDoList.listar_tarefas()

                case 0:
                    print("SAINDO ...")
                    print("------")
                    sair = True
                
                case _:
                    ("Valor inválido")


        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")