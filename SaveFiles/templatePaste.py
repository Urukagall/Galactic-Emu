# ce fichier sera supprimer, il ne sert qu'a reprendre ce qu'il y a dans les json template pour éviter de le faire a la main
from Functions.jsonReader import *

def templatePaste ():
    save = getAll("saveTemplate.json")
    postAll("save.json", save)
    
    upgrade = getAll("upgradeTemplate.json")
    postAll("upgrade.json", upgrade)