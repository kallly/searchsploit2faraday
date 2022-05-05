import json


target = '192.168.122.195'

f = open('ploit.json')
data = f.read().replace('\n}\n\n\n{\n', '},{')
data = '[' + data + ']'
services = json.loads(data)

print('confirmed,severity,target,name,desc')

for service in services:
    for key in service.keys():
        if key.startswith('RESULTS_'):
            for vuln in service[key]:
                name = vuln['Title'].replace("'","\'").replace('"','\"').replace(',','')
                print('False,unclassified,"'+target+'","'+ name + '","EDB-ID: ' + vuln['EDB-ID'] + '\nDate: ' + vuln['Date'] + '\nAuthor: ' + vuln['Author'] + '\nType: ' + vuln['Type']+ '\nPath: ' + vuln['Path'] + '"')