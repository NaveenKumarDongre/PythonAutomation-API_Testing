import configparser
from pathlib import Path 

cfgFile = 'petsqa.ini'
cfgFileDir = 'config'

config = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE =  BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
print(CONFIG_FILE)

config.read(CONFIG_FILE)


def getPetAPIURL():
    return config['pet']['url']

def getStoreAPIURL():
    return  config['store']['url']

print(getPetAPIURL())
print(getStoreAPIURL())
