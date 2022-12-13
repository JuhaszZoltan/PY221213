nev:str = input('írj be egy nevet: ')
mp:int = int(input('maximális pontszám: '))
ep:int = int(input('elért pontszám: '))

if ep > mp:
    print('HIBA, az elért pontszám nem lehet magasabb, mint a maximális pontszám!')
else:
    sz:float = ep / mp * 100
    if   sz < 51: oszt:str = 'elégtelen'
    elif sz < 65: oszt:str = 'elégséges'
    elif sz < 77: oszt:str = 'közepes'
    elif sz < 90: oszt:str = 'jó'
    else:         oszt:str = 'jeles'
    print(f'{nev} {round(sz, 1)}%-ot ért el, osztályzata: {oszt}')