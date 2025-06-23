kommer ={
    'naam' : 'Kommer',
    'leeftijd' : 35,
    'stad' : 'Sint Hubert',
    }

alt = dict(naam = 'Lisa', leeftijd = 34, stad = 'Sint Hubert')

print(f'Hallo, ik ben {kommer['naam']} en ik woon in {kommer['stad']}.')

kommer['beroep'] = 'groenteman'

print(kommer)

kommer['beroep'] = 'programmeur'

print(kommer)

for key, value in kommer.items():
    print(f'Key is {key}, value is {value}')

beroep = kommer.pop('leeftijd')
print(beroep)

kommer['hobbies'] = ['tijd met familie doorbrengen', 'voetbal', 'gamen']
print(kommer)

###################################################################################
print('############################################################################')


nummers = {3,2,1,3,5}
lijst = ['Moeder', 'Vader', 'Dochter']
namen_set = set(lijst)

print(namen_set)

namen_set.add('Zoon')

print(namen_set)

verschil = nummers.difference({4,5,6,7})

print(verschil)

intersectie = nummers.intersection((3,1,6,7,5))

print(intersectie)

