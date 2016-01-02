import json

fil = open('datafile.json','r')
data = fil.read()

datadict = json.loads(data)

print(datadict)
