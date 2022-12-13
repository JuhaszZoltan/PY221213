from random import randint

pontszam:int = 0
for i in range(5):
    print(f'{i+1}. kör:')
    x:int = randint(10, 99)
    y:int = randint(10, 99)
    ossz:int = x + y
    kul:int = x - y
    if kul < 0: kul *= -1
    print(f'a két szám összege: {ossz}')
    print(f'a két szám különbsége: {kul}')
    print('mi lehet az eredeti két szám?')
    x_tipp:int = int(input('egyik: '))
    y_tipp:int = int(input('másik: '))
    if (x == x_tipp and y == y_tipp) or (x == y_tipp and y == x_tipp):
        print('így van!')
        pontszam += 1
    else: print(f'nem :( a két szám a {x} és {y}')

print(f'végeztünk, összesen {pontszam} alkalommal adtál helyes választ!')