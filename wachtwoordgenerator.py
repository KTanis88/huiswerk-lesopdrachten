import random
import string

print("Welkom bij de wachtwoordgenerator van Kommer!!!!")

# # Vraag de gebruiker om invoer
# aantal_letters = int(input("Hoeveel letters wil je in je wachtwoord hebben? \n "))
# aantal_cijfers = int(input(" Hoeveel cijfers wil je in je wachtwoord hebben? \n "))
# aantal_symbolen = int(input(" Hoeveel symbolen wil je in je wachtwoord hebben? \n "))
#
# wachtwoord = []
#
# # Voeg letters toe
# for _ in range(aantal_letters):
#     wachtwoord.append(random.choice(string.ascii_letters))
#
# # Voeg cijfers toe
# for _ in range(aantal_cijfers):
#     wachtwoord.append(random.choice(string.digits))
#
# # Voeg symbolen toe
# for _ in range(aantal_symbolen):
#     wachtwoord.append(random.choice(string.punctuation))
#
# # Maak het wachtwoord als string, in vaste volgorde
# eenvoudig_wachtwoord = ''.join(wachtwoord)
# print(f"Hier is je eenvoudige wachtwoord: {eenvoudig_wachtwoord}")

# Vraag de gebruiker om invoer
aantal_letters = int(input("Hoeveel letters wil je in je wachtwoord hebben? \n "))
aantal_cijfers = int(input(" Hoeveel cijfers wil je in je wachtwoord hebben? \n "))
aantal_symbolen = int(input(" Hoeveel symbolen wil je in je wachtwoord hebben? \n "))

wachtwoord = []

# Voeg letters toe
for _ in range(aantal_letters):
    wachtwoord.append(random.choice(string.ascii_letters))

# Voeg cijfers toe
for _ in range(aantal_cijfers):
    wachtwoord.append(random.choice(string.digits))

# Voeg symbolen toe
for _ in range(aantal_symbolen):
    wachtwoord.append(random.choice(string.punctuation))

# Hussel alles door elkaar
random.shuffle(wachtwoord)

# Maak het wachtwoord als string, in vaste volgorde
moeilijk_wachtwoord = ''.join(wachtwoord)
print(f"Hier is je moeilijke wachtwoord: {moeilijk_wachtwoord}")