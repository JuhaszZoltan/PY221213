a:int = int(input('a háromszög "a" oldalának hossza (cm): '))
b:int = int(input('a háromszög "b" oldalának hossza (cm): '))
c:int = int(input('a háromszög "c" oldalának hossza (cm): '))

if (a+b<=c) or (a+c<=b) or (b+c<=a):
    print('ilyen oldalhosszakkal nem szerkeszthető 3szög!')
else:
    s:float = (a + b + c) / 2
    t:float = (s*(s-a)*(s-b)*(s-c)) ** .5
    print(f'a háromszög területe: {round(t, 4)} cm^2')