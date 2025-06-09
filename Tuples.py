tuple_of_numbers = (1, 2, 3, 4, 5)
tuple_of_names = ('Alice', 'Bob', 'Charlie')
tuple_miced = (1, 'Alice', True, 2.3)

print(tuple_of_numbers[1])
print(tuple_of_names[-1])

tuple_of_numbers2 = (2, 2, 3, 3, 2)

print(tuple_of_numbers2.count(2))
print(tuple_of_numbers2.index(2))

print(f'De middelste 3 nummers uit de lijst zijn:{tuple_of_numbers[1:4]}')
print(f'De eerste 3 nummers uit de lijst zijn:{tuple_of_numbers[:3]}')
print(f'De tweede en de een-na-laatste:{tuple_of_numbers[1::2]}')

print('-----------------------------------------------------------------------')
slicing_tuple = ('banaan', 'appel', 'peer', 'citroen', 'papaya')
print(slicing_tuple[0])
eerste_drie = slicing_tuple[0:3:1]
print(eerste_drie)

boodschappenlijst = ('kaas', 'melk', 'tomaten', 'hondenvoer', 'gehakt', 'kip',
                     'wasverzachter', 'hagelslag', 'pindakaas', 'brood')
print(f'De middelste twee items uit de lijst zijn: {boodschappenlijst[4:6:1]}')


