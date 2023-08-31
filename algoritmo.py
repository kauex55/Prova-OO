from classes import *
import os

def main():

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---MENU---")
            print("01 - ADICIONAR TAREFAS")
            print("02 - EXCLUIR TAREFAS")
            print("03 - LISTAR TAREFAS")


            print("Qual opção deseja?")
            menu = int(input(">> "))
            os.system("pause")

            match menu:
                case 1:
                    os.system("cls")
                    print("---ADICIONAR TAREFAS---")
                    print("INFORME SUA TAREFA")
                    descricao = input(">> ")



        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")