prijs = int(input('Wat is de artikelprijs? '))
bedrag = int(input('Welk bedrag wordt er betaald? '))

if bedrag < prijs:
    print('Te weinig betaald.')
else:
    wisselgeld = bedrag - prijs

    vijfeuro = wisselgeld // 5
    rest = wisselgeld % 5
    tweeeuro = rest / 2
    eeneuro = rest % 2

    print('Geef', vijfeuro , 'biljetten van vijf euro.')
    print('Geef', tweeeuro, 'stukken van twee euro.')
    print('Geef', eeneuro, 'stukken van één euro.')