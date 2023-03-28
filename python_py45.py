lista = []
osszeg = 0
szam = 3
IGAZ = False

if szam >= -5 and szam <= 5:
    IGAZ = True
    while IGAZ == True:
        szam = int(input('Kérek egy számot ami a [-5;5] intervallumban van! Ha kiakarsz lépni adj meg egy számot ami az intervallumból kiesik. '))
        if szam >= -5 and szam <= 5:
            lista.append(szam)
            if szam >= 0:
                osszeg += szam
            else:
                osszeg += szam
        if szam <= -6 or szam >= 6:
            IGAZ = False
            
print(lista)
print(osszeg)