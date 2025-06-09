boodschappenlijst = ('kaas', 'melk', 'tomaten', 'hondenvoer', 'gehakt', 'kip',
                     'wasverzachter', 'hagelslag', 'pindakaas', 'brood')
print(f'Het eerste en derde item van de lijst is :{boodschappenlijst[0]} en {boodschappenlijst[2]}.')

benodigde_boodschappen = [boodschappenlijst[i] for i in [0,2]]
print(benodigde_boodschappen)