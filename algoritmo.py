from classes import *
import os

def main():
    contID = 0
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
                    os.system("cls")
                    print("---ADICIONAR TAREFAS---")
                    print("INFORME SUA TAREFA")
                    contID += 1
                    id = contID
                    descricao = input(">> ")

                    ToDoList.adicionar_tarefa(id, descricao)
                    
                    print("TAREFA SALVA")
                    print("--------")
                    os.system("pause")

                
                
                case 3:

                    os.system("cls")
                    print("LISTA DE TAREFAS")
                    ToDoList.listar_tarefas()
                    os.system("pause")

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