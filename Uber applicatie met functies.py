# Dictionary met diensten en prijzen per kilometer

uber_diensten = {1: {'naam': 'Uber black','prijs': 2.00},
                 2:{'naam': 'Uber van', 'prijs':3.50},
                 3:{'naam': 'Uber X', 'prijs':1.50}}

def toon_menu():
    print('Kies het type Uber:')
    for nummer, dienst in uber_diensten.items():
        print(f'{nummer}. {dienst['naam']}(€{dienst['prijs']:.2f} per kilometer)')
        print('---------------')

def get_user_choice():
    while True:
        try:
            keuze = int(input('Voer het nummer van uw keuze in:'))
            if keuze in uber_diensten:
                return keuze
            else:
                print('Ongeldige keuze, probeer opnieuw.')
        except ValueError:
            print('Voer een geldig nummer in.')

def get_kilometers():
    while True:
        try:
            km = float(input('Voer het aantal kilometers van uw rit in:'))
            if km > 0:
                return km
            else:print('Het aantal kilometers moet positief zijn.')
        except ValueError:
             print('Voer een geldig getal in.')

def bereken_kosten(prijs_per_km, kilometers):
    return prijs_per_km * kilometers

# Hoofdprogramma
toon_menu()
keuze = get_user_choice()
kilometers = get_kilometers()

dienst = uber_diensten[keuze]
kosten = bereken_kosten(dienst['prijs'], kilometers)

print(f'U heeft gekozen voor {dienst['naam']}. De kosten voor uw rit van {kilometers:.0f} kilometer(s) zijn €{kosten:.2f}')



