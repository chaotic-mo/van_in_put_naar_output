
#min = 45
#persoon = 4
#gmin = 5

#tickets = 7.45
#gameseat = 0.37

#print(persoon * tickets + ((min / gmin) * gameseat * persoon))

print('de gegevens van speelhal ')
tickets = input('hoeveel kost de tickets? ')
gameseat = input('hoeveel kost de gameseats? ')
pp = input('hoeveel personen zijn er? ')

min =  input('hoeveel minuten? ')
gmin =  input('hoeveel game minuten? ')

totaal = (int(pp) * float(tickets) + ((int(min) / int(gmin)) * float(gameseat) * int(pp)))

print('''  ----------------------------------------------------''')
print(' | tickets       : ' + tickets )
print(' | gameseat      : ' + gameseat)
print(' | pp            : ' + pp)
print(' | min           : ' + gameseat)
print(' | gmin          : ' + gmin)
print(' | totaal        : ' + str(totaal))
print('''  ----------------------------------------------------''')