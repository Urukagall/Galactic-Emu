import json

def getAll (fileName):
    with open('SaveFiles/' + str(fileName), 'r') as f:
        data = json.load(f)
    return data

def get (fileName, var):
    with open('SaveFiles/' + str(fileName), 'r') as f:
        data = json.load(f)
    return data[str(var)]

def post (fileName, var, value):
    with open('SaveFiles/' + str(fileName), 'r') as f:
        data = json.load(f)
    data[var] = value

    with open('SaveFiles/' + str(fileName), 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))  
        
def postAll (fileName, value):
    with open('SaveFiles/' + str(fileName), 'r') as f:
        data = json.load(f)
    data = value

    with open('SaveFiles/' + str(fileName), 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))