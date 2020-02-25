class AnonymousSurvey():
    """ Coleta respostas anônimas para uma pergunta de uma pesquisa. """


    def __init__(self, question):
        """ Armazena uma pergunta e se prepara para armazenar as respostas. """
        self.question = question
        self.responses = []


    def show_question(self):
        """ Mostra a pergunta da pesquisa. """
        print(self.question)


    def store_response(self, *new_response):
        """ Armazena várias respostas para cada pessoa. """
        for response in new_response:
            self.responses.append(response)


    def show_results(self):
        """ Mostra todas as respostas dadas. """
        print("Survey results:")
        for response in self.responses:
            print("- " + response)