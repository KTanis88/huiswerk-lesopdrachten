# Oefening 1: Gemiddelde berekenen

def bereken_gemiddelde(getallen) :
    if not getallen :
        return 0
    return sum(getallen) / len(getallen)

# Bijvoorbeeld:

lijst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(f" Het gemiddelde is : {bereken_gemiddelde(lijst)}")


# Oefening 2: Woorden tellen

def tel_woorden(zin) :
    woorden = zin.split()
    return len(woorden)

# Extra: interactieve invoer

zin = input("Voer een zin in: ")
print(f"Aantal woorden: {tel_woorden(zin)}")


# Oefening 3: Palindroom

def is_palindroom(woord) :
    woord = woord.lower()
    return woord == woord[: :-1]

# Extra : palindroom voor een zin
# Verwijder spaties en maak hoofdletterongevoelig
def is_palindroom_zin(zin) :
    zin_schoon = ''.join(char.lower() for char in zin if char.isalnum())
    return zin_schoon == zin_schoon[: :-1]

# Bijvoorbeeld:
woord = input("Voer een woord in: ")
if is_palindroom(woord) :
    print(f"{woord} is een palindroom! ")
else:
    print(f"{woord} is geen palindroom! ")

# Extra voor zinnen:
zin = input("Voer een zin in: ")
if is_palindroom_zin(zin) :
    print("Deze zin is een palindroom! ")
else:
    print("Deze zin is geen palindroom! ")


# Oefening 4: Bibliotheek

# Bibliotheek als lijst van dictionaries

bibliotheek = []

def voeg_boek_toe(titel, auteur, genre):
    boek = {"titel": titel, "auteur": auteur, "genre": genre }
    bibliotheek.append(boek)

def zoek_op_genre(gezocht_genre) :
    return [boek for boek in bibliotheek if boek["genre"].lower() == gezocht_genre.lower() ]

def toon_alle_boeken():
    if not bibliotheek:
        print("Er zijn nog geen boeken in de bibliotheek.")
    for boek in bibliotheek:
        print(f"{boek['titel']} door {boek['auteur']} ({boek['genre']})")


# interactief menu
while True :
    print("\n1. Boek toevoegen\n2. Zoeken op genre\n3. Alle boeken weergeven\n4. Stoppen")
    keuze = input("Maak een keuze")
    if keuze == "1":
        titel = input("Titel: ")
        auteur = input("Auteur: ")
        genre = input("Genre: ")
        voeg_boek_toe(titel, auteur, genre)
        print("Boek toegevoegd!!")
    elif keuze == "2" :
        genre =  input("Welk genre zoek je? ")
        gevonden = zoek_op_genre(genre)
        if gevonden:
            for boek in gevonden:
                print(f"{boek['titel' ]} door {boek['auteur ']} ({boek['genre ']}")
        else:
            print("Geen boeken gevonden in dit genre.")
    elif keuze == "3":
        toon_alle_boeken()
    elif keuze == "4":
        print("Tot ziens!")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")


