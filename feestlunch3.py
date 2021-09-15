#anc = 17
#ans = 2
#ank = 3

#croissantje = 0.39
#stokbroden = 2.78
#kortingsbonnen = 0.50

#print(anc * croissantje + (ans * stokbroden) - (ank * kortingsbonnen))

croissantje = input('hoeveel kost de criossantjes? ')
stokbroden = input('hoeveel kost de stokbroden? ')
kortingsbonnen = input('hoeveel zijn de kortingsbonnen? ')

anc = input('hoeveel croissantjes? ')
ans = input('hoeveel stokbroden? ')
ank = input('hoeveel kortingsbonnen? ')

totaal = (int(anc) * float(croissantje) + (int(ans) * float(stokbroden)) - (int(ank) * float(kortingsbonnen)))

print('''  ----------------------------------------------------''')
print(' | croissantje     : ' + croissantje )
print(' | stokbroden      : ' + stokbroden)
print(' | kortingsbonnen  : ' + kortingsbonnen)
print(' | anc             : ' + anc)
print(' | ans             : ' + ans)
print(' | ank             : ' + ank)
print(' | totaal          : ' + str(totaal))
print('''  ----------------------------------------------------''')

