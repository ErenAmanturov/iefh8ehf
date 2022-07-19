data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
operations = {}
b = 0
while len(operations) != len(designations):
    operations[designations[b]] = codes[b]
    b += 1
del operations['Katel'], operations['Fonex']
operations['O!'] = {'0705', '0700', '0500'}
operations['Megacom'] = {'0550', '0999', '0555'}
operations['Beeline'] = {'0770', '0222', '0777'}
for k, v in operations.items():
    print(f'{k} - {v}')
