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
#from Tuples1 import student

#Maak een applicatie die het volgende kan:
#Een lijst van studenten en cijfers opslaan.
#Studenten en hun cijfers weergeven.
#Het gemiddelde cijfer berekenen.

#Een lijst van studenten en cijfers opslaan.
Student = (('Kommer', 6.4), ('Lisa', 7.1), ('Isabella', 9.8), ('Kommer jr.', 10), ('Khloe', 8.6), ('Phileine', 9.2), ('Mufasa', 4.4), ('Teddy', 5.8))

#Studenten en hun cijfers weergeven.
studenten_lijst = list(Student)
studenten_lijst = sorted(studenten_lijst, key=lambda x: x[1], reverse=True)
for naam, cijfer in studenten_lijst:
    print(f'Naam: {naam}', f'Cijfer: {cijfer}')

#Het gemiddelde cijfer berekenen en de beste student.
totaal = sum(cijfer for _, cijfer in studenten_lijst)
aantal = len(studenten_lijst)
gemiddelde = totaal/aantal
beste_student = max(studenten_lijst, key=lambda x: x [1])
print(f'Het gemiddelde cijfer is: {gemiddelde:.2f}')
print(f'De beste student is', beste_student[0], 'met een', beste_student[1])

#Student toevoegen
naam = input('Voer de naam van de nieuwe student in: ')
cijfer = float(input('Voer het cijfer in: '))
studenten_lijst.append((naam, cijfer))

#Zoeken op naam
zoeknaam = input('Voer de naam in die je wilt zoeken: ')
gevonden = [ (naam, cijfer) for naam,cijfer in studenten_lijst if naam.lower() == zoeknaam.lower()]
if gevonden:
    for naam, cijfer in gevonden:
        print(f'Gevonden: {naam}, Cijfer;{cijfer}')
else:
    print('Student niet gevonden.')



