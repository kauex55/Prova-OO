class ToDoList:
    def adicionar_tarefa(self, descricao):
        self.descricao = descricao
 
    def excluir_tarefa(self, indice):
        del self

    def listar_tarefas(self):
        print(self.descricao)