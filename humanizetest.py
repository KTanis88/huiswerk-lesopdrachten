import humanize
import datetime

# Humanize schrijft dingen dusdanig op dat het makkelijk voor mensen te lezen is.
# Bijvoorbeeld grote getallen of data

#Grote getallen als woorden
print(humanize.intword(392424742))

#Grote getallen met komma's
print(humanize.intcomma(12458493932))

#Maar bijvoorbeeld ook in tijdsduur
print(humanize.naturaltime(datetime.datetime.now()- datetime.timedelta(hours=6)))

print(humanize.naturaldate())