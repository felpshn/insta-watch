from .app import InstaFollow
from .util import clearScreen

if __name__ == '__main__':
  clearScreen()
  print('█'*10, ' InstaFollow ', '█'*10)
  accountCredentials = []
  accountCredentials.append(str(input('\n> Username: ')))
  accountCredentials.append(str(input('> Password: ')))
  InstaFollow(accountCredentials).run()
