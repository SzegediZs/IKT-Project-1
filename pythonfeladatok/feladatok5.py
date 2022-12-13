
bekertSzam1=int(input("Adj meg egy számot: "))
bekertSzam2=int(input("Adj meg még egy számot: "))
sor = 1
while sor <= bekertSzam1:
    oszlop = 1
    while oszlop <= bekertSzam2:
        print('*', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1
        