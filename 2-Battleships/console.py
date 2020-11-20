from os import system, name

def clearConsole():
    """
    Summary:
    Method to clear console from previous outputs.
    """

    if name == 'nt':
        system('cls')
    else:
        system('clear')