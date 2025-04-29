keys = ['name', 'last name', 'age']
values = ['Guido', 'van Rossum', '60']

d = dict(zip(keys, values)) #Create the dictionary

'''for k in d:
    info = '{}: {}'.format(k, d[k])


#formatted text with keys and values

print(info)'''

for k,v in d.items():
    # d.items returns duobles with key, value
    print('{}: {}'.format(k, v))
