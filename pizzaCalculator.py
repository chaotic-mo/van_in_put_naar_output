#small = €3.50
#midium = €5.00
#large = €100.00

small = input("hoeveel small pizza's wilt u? ")
midium = input("hoeveel midium pizza's wilt u? ")
large = input("hoeveel large pizza's wilt u? ")

Small_Price = float(3.50)
Midium_Price = float(5.00)
Large_Price = float(100.00)

Small_Som = Small_Price * int(small)
Midium_Som = Midium_Price * int(midium)
Large_Som = Large_Price * int(large)

totaal = Small_Som + Midium_Som + Large_Som

print('''  ----------------------------------------------------''')
print(' | de koste voor small       € ' + str(Small_Price)  +   '   hoeveel    : '  + small     +  ' koste    :  '  + str(Small_Som))
print(' | de koste voor midium      € ' + str(Midium_Price) +   '   hoeveel    : '  + midium    +  ' koste    :  '  + str(Midium_Som))
print(' | de koste voor large       € ' + str(Large_Price)  +   '   hoeveel    : '  + large     +  ' koste    :  '  + str(Large_Som))
print('''  ----------------------------------------------------''')
print(' | de totale koste           € ' + str(totaal))
print('''  ----------------------------------------------------''')

