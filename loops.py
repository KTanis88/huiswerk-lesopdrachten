# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Probeer het eerst zonder loop,
# nummer = int(input('Voer een cijfer in:'))
# print(nummer, '* 1=', (nummer * 1))
# print(nummer, '* 2=', (nummer * 2))
# print(nummer, '* 3=', (nummer * 3))
# print(nummer, '* 4=', (nummer * 4))
# print(nummer, '* 5=', (nummer * 5))
# print(nummer, '* 6=', (nummer * 6))
# print(nummer, '* 7=', (nummer * 7))
# print(nummer, '* 8=', (nummer * 8))
# print(nummer, '* 9=', (nummer * 9))
# print(nummer, '* 10=', (nummer * 10))
#
# # Probeer het nu met een loop.
#
# getal = int(input('Voer een cijfer in:'))
# for i in range(1, 11):
#     print(getal, 'x', i, '=', getal * i)


# --------------------------------------------------------------------------------------------

# # Optellen
# # Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.
#
# # Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)
#
# limiet = int(input('Voer een limiet in:'))
# teller = 1
# som = 0
# while teller <= limiet:
#     som += teller
#     teller += 1
#
# print('De som van getallen tot', limiet, 'is', som)
# # --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.
# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.
# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizzbuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)



# --------------------------------------------------------------------------------------------


# Fibonacci-reeks

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1.
# Elk volgend getal is de som van de twee voorgaande.
# De eerste 10 getallen van de Fibonacci-reeks zijn:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13
# 8 + 13 = 21
# 13 + 21 = 34

i = int(input("Hoeveel Fibonacci-getallen wil je zien? "))

# De eerste twee getallen van de Fibonacci-reeks zijn 0 en 1
a = 0
b = 1

# Eerst drukken we de eerste twee getallen af
print(a)
print(b)

# Vervolgens berekenen we de volgende getallen en drukken ze af
for _ in range(2, i):
    c = a + b
    print(c)
    a = b
    b = c