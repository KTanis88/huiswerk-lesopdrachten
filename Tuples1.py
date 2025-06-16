steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk
print (steden[0])
print (steden[1])
print (steden[2])
print (steden[3])
print (steden[4])
print (steden[5])
print (steden[-1])
# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple

tuple_compleet = (tuple1 + tuple2)

print (tuple_compleet)

# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)
mijn_tuple = (1, 2, 3, 4, 'a', 'b', 'c', 'd', False, True, None, 1.1, 1.2, 1.3, 1.4)

# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element
print (mijn_tuple[0])
print (mijn_tuple[1:5])
print (mijn_tuple[-1])
# --------------------------------------------------------------------------------------------


# Maak een tuple met een naam en een leeftijd
student = ('Kommer', 36)

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)
naam, leeftijd = student


# Print de uitgepakte variabelen
print('Naam',naam)
print('Leeftijd',leeftijd)