namen = ['papa', 'mama', 'zoon', 'dochter']

def toCapitalString(lijst):
    capitalized = []
    for item in lijst:
        capitalized.append(item.capitalize())
    firstpart = capitalized[0:-1]
    lastpart = capitalized[-1:]

    if firstpart:
            return f"{', '.join(firstpart)} en {lastpart[0]}"
    else:
            return lastpart

print(toCapitalString(namen))