def verwerk_namen(namen_lijst):
    # Zet elke naam met een hoofdletter
    namen_lijst = [naam.capitalize() for naam in namen_lijst]
    if not namen_lijst:
        return ""
    if len(namen_lijst) == 1:
        return namen_lijst[0]
    #Namen combineren met komma's.(Behalve de laatste)
    eerste_vijf = ",".join(namen_lijst[:-1])
    #De laatste naam toevoegen met een en.
    return f"{eerste_vijf} en {namen_lijst[-1]}"

# Mijn namen
namen_lijst =  ['kommer', 'lisa', 'isabella', 'kommer jr.', 'khloe', 'phileine']
resultaat = verwerk_namen(namen_lijst)
print(resultaat)







