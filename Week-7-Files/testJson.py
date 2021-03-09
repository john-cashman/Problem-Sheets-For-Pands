import json
filename="testdict.json"
sample= dict(name='Bob',age=32, grades=[21,54,59])

def writeDict(obj):
    with open(filename, 'a') as f:
        json.dump(obj,f)

writeDict(sample)