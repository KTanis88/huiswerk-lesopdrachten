# Dictionary met diensten en prijzen per kilometer

uber_diensten = {1: {'naam': 'Uber black','prijs': 2.00},
                 2:{'naam': 'Uber van', 'prijs':3.50},
                 3:{'naam': 'Uber X', 'prijs':1.50}}

def toon_menu():
    print('Kies het type Uber:')
    for nummer, dienst in uber_diensten.items():
        print(f"{nummer}. {dienst['naam']}(€{dienst['prijs']:.2f} per kilometer)")
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

print(f"U heeft gekozen voor {dienst['naam']}. De kosten voor uw rit van {kilometers:.0f} kilometer(s) zijn €{kosten:.2f}")


# Bonus: Voorkeursdienst instellen en gebruiken
voorkeursdienst = None #Hier komt het nummer van de voorkeursdienst.

#Instellen van de voorkeursdienst
def stel_voorkeursdienst_in():
    global voorkeursdienst
    print('\n Voorkeursdienst instellen:')
    print('1. Uber Black')
    print('2. Uber Van')
    print('3. Uber X')
    keuze = input('Kies uw voorkeursdienst(1-3):')
    if keuze in ['1','2','3']:
        voorkeursdienst = int(keuze)
        print('Voorkeursdienst opgeslagen.')
    else:
        print('Ongeldige keuze.')

#Gebruiken van de voorkeursdienst bij het boeken van een rit

def vraag_om_voorkeur():
    global voorkeursdienst
    if voorkeursdienst:
        gebruik = input(f"Uw voorkeursdienst is {uber_diensten[voorkeursdienst]['naam']}. Wilt u deze gebruiken? (j/n):").lower()
        if gebruik == 'j':
            return voorkeursdienst
    return None # Om te voorkomen dat het bestaande keuzeproces blijft lopen.

# Bonus: Ritgeschiedenis bijhouden
ritgeschiedenis = []

def voeg_rit_toe(dienstnaam, kilometers, kosten):
    ritgeschiedenis.append({'dienst': dienstnaam,
                            'kilometers': kilometers,
                            'kosten': kosten})

def toon_ritgeschiedenis():
    if not ritgeschiedenis:
        print('Er zijn nog geen ritten gemaakt.')
    else:
        print('\n Ritgeschiedenis:')
        for i, rit in enumerate(ritgeschiedenis,1):
            print(f"{i}. {rit['dienst']} - {rit['kilometers']} km - €{rit['kosten']:.2f}")
            
# #Stel de voorkeursdienst in
# stel_voorkeursdienst_in()
#
# #Vraag of je de voorkeursdienst wil gebruiken, anders kies je handmatig
# keuze = vraag_om_voorkeur()
# if not keuze :
#     toon_menu()
#     keuze = get_user_choice()
#
# #Vraag het aantal kilometers
# kilometers = get_kilometers()
#
# #bereken de kosten en resultaat printen
# dienst = uber_diensten[keuze]
# kosten = bereken_kosten(dienst['prijs'], kilometers)
# print(f'U heeft gekozen voor {dienst['naam']}. De kosten voor uw rit van {kilometers:.0f} '
#       f'kilometers zijn €{kosten:.2f}.')
#
# # Toevoegen rit aan de geschiedenis.
# voeg_rit_toe(dienst['naam'], kilometers, kosten)
#
# #Toon de ritgeschiedenis
# toon_ritgeschiedenis()

#Hoofdmenu
while True:
    print('\n--- Uber Boeksysteem ---')
    print('1. Boek een rit')
    print('2. Stel voorkeursdienst in')
    print('3. Bekijk ritgeschiedenis')
    print('4. Stoppen')
    keuze = input('Maak een keuze (1-4):')
    if keuze == '1' :
        voorkeur = vraag_om_voorkeur()
        if voorkeur:
            gekozen = voorkeur
        else:
            toon_menu()
            gekozen = get_user_choice()
        kilometers = get_kilometers()
        dienst =  uber_diensten[gekozen]
        kosten = bereken_kosten(dienst['prijs'], kilometers)
        print(f"U heeft gekozen voor {dienst['naam']}. De kosten voor uw rit van {kilometers:.0f}"
              f" kilometers zijn €{kosten:.2f} ")
        voeg_rit_toe(dienst['naam'], kilometers, kosten )
    elif keuze == '2' :
        stel_voorkeursdienst_in()
    elif keuze == '3' :
        toon_ritgeschiedenis()
    elif keuze == '4' :
        print('Tot ziens!')
        break
    else:
        print('Ongeldige keuze.')



