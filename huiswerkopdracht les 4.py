# numbers = [1, 2, 3, 4, 5]
#
#
# for number in numbers:
#     if number == 3:
#         break
#
#         print(f"Number is {number}")
#
#         print('Out of loop')
#
# for number in numbers:
#     if number == 3:
#         continue
#
#         print('Number is' + str(number))
#
#         print('Out of loop')
from Tuples1 import student

#Maak een appplicatie die het volgende kan:
#Een lijst van studenten en cijfers opslaan.
#Studenten en hun cijfers weergeven.
#Het gemiddelde cijfer berekenen.

#Een lijst van studenten en cijfers opslaan.
Student = ('Kommer', 6.4, 'Lisa', 7.1, 'Isabella', 9.8, 'Kommer jr.', 10, 'Khloe', 8.6, 'Phileine', 9.2, 'Mufasa', 4.4, 'Teddy', 5.8)

#Studenten en hun cijfers weergeven.
studenten_lijst = [(Student[i], Student[i+1]) for i in range(0, len(Student), 2)]

for naam, cijfer in studenten_lijst:
    print(f'Naam: {naam}', f'Cijfer: {cijfer}')

#Het gemiddelde cijfer berekenen.
totaal = sum(cijfer for _, cijfer in studenten_lijst)
aantal = len(studenten_lijst)
gemiddelde = totaal/aantal
print(f'Het gemiddelde cijfer is: {gemiddelde:.2f}')

