def fazer_sanduiche(*ingredientes):
    """ Exibe a lista de ingredientes de um sanduíche. """
    print("\nO sanduíche é composto dos seguintes ingredientes:")
    for ingrediente in ingredientes:
        print("- " + ingrediente)

fazer_sanduiche('queijo')
fazer_sanduiche('presunto', 'quiejo')
fazer_sanduiche('maionese', 'presunto', 'queijo')