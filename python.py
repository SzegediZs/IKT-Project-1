"""def feladat1():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot:")))

    print(min(tomb))

feladat1()"""

"""def feladat2():
    tomb =[]

    for i in range(3):
        tomb.append(int(input("Kérek egy számot:")))

    print(max(tomb))

feladat2()"""


"""def feladat3():
    pontSzam=int(input("Kérem a pontszámot:"))

    if pontSzam < 50 :
        print("Érdemjegy:1")
    if pontSzam >= 50 and pontSzam < 60 :
        print("Érdemjegy:2")
    if pontSzam >= 60 and pontSzam < 70 :
        print("Érdemjegy:3")
    if pontSzam >= 70 and pontSzam < 85 :
        print("Érdemjegy:4")
    if pontSzam > 85 :
        print("Érdemjegy:5")

feladat3()"""

"""def feladat4():

    bekertSzam=int(input("Adj meg egy egész számot:"))

    if bekertSzam % 3 == 0 :
        print ("Osztható 3-mal.")
    if bekertSzam % 5 == 0 :
        print ("Oszthato 5-el")
    if bekertSzam % 3 != 0 and bekertSzam % 5 != 0 :
        print("Nem oszható 3-mal és 5-el sem.")

feladat4()"""

def feladat5():

    bekertSzam=[]
    for i in range (3): 
        bekertSzam=int(input(f"Adj meg egy számot:"))

    if (bekertSzam[0]) + (bekertSzam[1]) == (bekertSzam[2]):
        print("Az első és a második szám összege a harmadik szám.")

feladat5()






