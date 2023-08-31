class ToDoList:
    def adicionar_tarefa(self, descricao, id):
        self.id = id
        self.descricao = descricao
        self.a = {}
        self.a[self.id] = [self.descricao]

    def excluir_tarefa(self, indice):
        self.indice = indice

    def listar_tarefas(self):
        for chave,a in self.reserva.items():
            print(f"ID:{chave} - Tarefas:{a}")