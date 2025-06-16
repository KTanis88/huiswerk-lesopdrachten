PI = 3.14159

def bereken_inhoud_cilinder(straal = 5, hoogte = 10) :
    """Bereken de inhoud van een cilinder"""
    inhoud = PI * hoogte * straal ** 2
    return(inhoud)
print(bereken_inhoud_cilinder(0.5, 2))
print(bereken_inhoud_cilinder(hoogte=2))