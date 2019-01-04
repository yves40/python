# Baboule TP on list

titi = ['A', 'B', 'C', 'D']
toto = [ 1, 2, 3, 4]
for s in toto :
        print s
        
for s in titi:
        print s

toto.append(55)
titi.append('AZERTYUIOP')
titi.append(['AA', 'BB'])

print '------------------------------------------'
for s in titi:
        print s

titi.reverse()        
print '------------------------------------------'
for s in titi:
        print s

titi.remove('A')
print '------------------------------------------'
for s in titi:
        print s

print '------------ 2 levels --------------------'
for s in titi:
        for ss in s:
            print ss
