from selenium import webdriver
from os import name
from os.path import dirname, realpath, isfile

class Browser:
  def __init__(self):
    self.__supportedDrivers = [
      'msedgedriver.exe',
      'geckodriver',
      'geckodriver.exe',
      'chromedriver',
      'chromedriver.exe'
    ]
    self.__driverPath = ''
    self.__driverName = ''
    self.checkDriverExistence()


  def getSupportedDrivers(self):
    return self.__supportedDrivers


  def getDriverPath(self):
    return self.__driverPath


  def checkDriverExistence(self):
    if name == 'nt':
      srcDir = f'{dirname(realpath(__file__))}\\'
    else:
      srcDir = f'{dirname(realpath(__file__))}'
    for i in range(len(self.__supportedDrivers)):
      driverExists = f'{srcDir}{self.__supportedDrivers[i]}'
      if isfile(driverExists):
        self.__driverPath = driverExists
        self.__driverName = self.__supportedDrivers[i]
        break
      if i == len(self.__supportedDrivers) - 1:
        return False


  def setDriver(self):
    if self.__driverName == self.__supportedDrivers[0]:
      return webdriver.Edge
    elif self.__driverName == self.__supportedDrivers[i] or self.__driverName == self.__supportedDrivers[2]:
      return webdriver.Firefox
    elif self.__driverName == self.__supportedDrivers[3] or self.__driverName == self.__supportedDrivers[4]:
      return webdriver.Chrome
    else:
      raise Exception('\nCouldn\'t find a compatible webdriver in the source directory!')
