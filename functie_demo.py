lijst_met_afmetingen = [(10, 5), (7, 4), (3, 2), (5, 4)]

# oppervlaktes = []
# oppervlaktes.append(lijst_met_afmetingen[0][0] * lijst_met_afmetingen[0][1])
# oppervlaktes.append(lijst_met_afmetingen[1][0] * lijst_met_afmetingen[1][1])
# oppervlaktes.append(lijst_met_afmetingen[2][0] * lijst_met_afmetingen[2][1])
# oppervlaktes.append(lijst_met_afmetingen[3][0] * lijst_met_afmetingen[3][1])


# for x, y in lijst_met_afmetingen:
#     oppervlaktes.append(x*y)
#     print([str(oppervlakte) + " cm2" for oppervlakte in oppervlaktes ])


def oppervlakte(lijst):
    oppervlaktes = []
    for x,y in lijst:
        oppervlaktes.append(str(x*y) + " m2")
    return oppervlaktes

print(oppervlakte(lijst_met_afmetingen))

oppervlaktes = oppervlakte(lijst_met_afmetingen)

print(oppervlaktes)