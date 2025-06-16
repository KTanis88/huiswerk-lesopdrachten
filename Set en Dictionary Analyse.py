groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code",
"Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"]

groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight",
"The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"]

# 1. Unieke boeken
# 	•	Maak van beide lijsten een set om de unieke boeken per groep te bepalen.
# 	•	Print de unieke boeken voor beide groepen.

set_groep1 = set(groep1)
set_groep2 = set(groep2)

print('Unieke boeken groep 1:', set_groep1)
print('Unieke boeken groep 2:', set_groep2)

#  2. Gemeenschappelijke boeken
#	•	Welke boeken zijn door beide groepen geleend?
#	•	Gebruik de doorsnede (`intersection`) van de sets.

gemeenschappelijk = set_groep1.intersection(set_groep2)
print('Gemeenschappelijke boeken zijn:', gemeenschappelijk)

# 3. Boeken geleend door slechts één groep
#	•	Welke boeken zijn alleen door Groep 1 geleend en niet door Groep 2? Gebruik het verschil (`difference`).
#	•	Welke boeken zijn alleen door Groep 2 geleend en niet door Groep 1?

alleen_groep1 = set_groep1.difference(set_groep2)
alleen_groep2 = set_groep2.difference(set_groep1)
print('Boeken alleen geleend door groep 1 zijn:', alleen_groep1)
print('Boeken alleen geleend door groep 2 zijn:', alleen_groep2)

# 4. Aantal geleende keren per boek
#	•	Maak een dictionary voor elke groep met als sleutel het boek
#      	en als waarde het aantal keer dat het boek is geleend.

aantal_groep1 = {}
for boek in groep1:
    aantal_groep1[boek] = aantal_groep1.get(boek, 0) + 1

aantal_groep2 = {}
for boek in groep2:
    aantal_groep2[boek] = aantal_groep2.get(boek, 0) + 1

print('Aantal keren geleend per boek in groep 1 is:', aantal_groep1)
print('Aantal keren geleend per boek in groep 2 is:', aantal_groep2)

# 5. Meest geleende boek
#	•Gebruik de dictionary om te bepalen welk boek het meest is geleend per groep.

meest_groep1 = max(aantal_groep1, key=aantal_groep1.get)
meest_groep2 = max(aantal_groep2, key=aantal_groep2.get)

print('Welk boek is het meeste geleend in groep 1:', meest_groep1)
print('Welk boek is het meeste geleend in groep 2:', meest_groep2)

