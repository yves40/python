# Baboule TP on Dictionaries
# Syntax for the dictionary elements is a comma separated key:value elements

titi = { 'p1':'A', 'p2':'B', 'p3':'C', 'p4':'D' }
print titi.keys

print '------------------------------------------'
for s in titi:
        print 'Key : ', s, ' Value : ', titi[s]


print '------------------------------------------'
titi['p1'] = 'P1 is now AA'
for s in titi:
        print titi[s]

