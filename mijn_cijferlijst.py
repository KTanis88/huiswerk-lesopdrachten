mijn_cijferlijst = [1, 2, 3, 4, 5]
print(mijn_cijferlijst)
print(f'Het eerste item = {mijn_cijferlijst[0]}')
print(f'Het laatste item =' + str(mijn_cijferlijst[-1]))

mijn_cijferlijst.remove(3)

print(mijn_cijferlijst)

twee = mijn_cijferlijst.pop(1)
mijn_cijferlijst.append(twee)
mijn_cijferlijst.append(twee)
print(f'Het cijfer twee komt {mijn_cijferlijst.count(2)} keer voor.')

my_string = 'abcdefghijklmnopqrstuwvxyz'
print(my_string[int(input('Welke letter van het alfabet wil je zien?'))-1])

letterlijst = ['h', 'a', 'l', 'l', 'o']
print(letterlijst)
joined = ''.join(letterlijst)
print(joined)
