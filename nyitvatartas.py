ido = int(input('Hány óra van?  '))
if (ido >=8 and ido <= 16):
    print('A bolt nyitva van.')
    print('még ennyit van nyitva =',16 - ido,)
else:
    print('A bolt zárva van.')
    if (8 > ido ):
        print('ennyi ido van meg kinyit ez a geci:',8 - ido,)
    elif (16 < ido ):
        print('ennyi ido van meg kinyit:',24 - ido + 8,)
