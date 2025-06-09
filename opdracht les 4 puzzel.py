puzzel =  ['Albatros', 'poncho', 'vlinder', 'glitter']
coordinaten = [(0,0),(2,0),(0,-2),(1,3),(0,3),(2,4),(1,-1)]
# antwoord =  #coordinaat1 = 1e woord is albatros, 1e letter is a.
            #coordinaat2 = 3e woord is vlinder, 1e letter is v.
            #coordinaat3 = 1e woord is albatros, op een na laatste letter is o.
            #coordinaat4= 2e woord is poncho, 4e letter is c.
            #coordinaat5= 1e woord is albatros, 4e letter is a.
            #coordinaat6= 3e woord is vlinder, 5e letter is d.
            #coordinaat7= 2e woord is poncho , laatste letter is o.
            #Het antwoord= avocado

# Heb online opgezocht om er een code van te maken. Het lukte mij niet zelf om te bedenken
# om het bovenstaande in een code te maken.
# Defineer de lijst met woorden (puzzel) en de coordinaten.
puzzel =  ['Albatros', 'poncho', 'vlinder', 'glitter']
coordinaten = [(0,0),(2,0),(0,-2),(1,3),(0,3),(2,4),(1,-1)]

#Functie om een letter te ontcijferenw uit de puzzel op basis van een coordinaat.
def ontcijfer_letter(puzzel, coord):
    woord_index, letter_index = coord
    woord = puzzel[woord_index]
    return woord[letter_index]

# Ontcijfer het woord door alle coordinaten te verwerken.
antwoord = ''.join(ontcijfer_letter(puzzel,coord) for coord in coordinaten)

print(antwoord)
