from prettytable import PrettyTable, TableStyle

#prettytable zorgt voor het weergeven van tabellen in ASCII en export naar HTML/CSV

#Bijvoorbeeld

# tabel = PrettyTable()
# tabel.field_names = ["Club", "Teams", "Winst", "Verlies", "Gelijk"]
# tabel.add_row(["Vrc", "JO11-3", "5", "1", "2"])
# tabel.add_row(["Gvvv", "JO11-2", "2", "4", "2"])
# tabel.add_row(["Dovo", "JO11-2", "3", "4", "0"])
#
# print(tabel)
#
#
# #exporteren
# print(tabel.get_html_string())
# print(tabel.get_csv_string())

print("###################################################################################")


clubs = ['VRC', 'GVVV', 'DOVO', 'Roda 46', 'Hooglanderveen', 'Hoogland', 'Jonathan']
teams = ['JO11-3', 'JO11-1','JO11-2','JO11-2','JO11-2','JO11-2','JO11-3']
winst = [9, 7, 6, 5, 4, 3, 1]
gelijk = [2, 3, 4, 4, 4, 3, 2]
verlies = [1, 2, 2, 3, 4, 6, 9]

punten_per_winst = 3
punten_per_gelijk = 1
punten_per_verlies = 0

tabel = PrettyTable()
tabel.field_names = ["Clubs", "Teams", "Winst", "Gelijk", "Verlies", "Punten"]
tabel.set_style(TableStyle.PLAIN_COLUMNS)


for c, t, w, g, v, in zip(clubs, teams, winst, gelijk, verlies) :
    punten = w * punten_per_winst + g * punten_per_gelijk + v * punten_per_verlies
    tabel.add_row([c, t, w, g, v, punten])

print(tabel)

