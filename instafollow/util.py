from os import system, name

def clearScreen():
  if name == 'nt':
    system('cls')
  else:
    system('clear')
