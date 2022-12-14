def halHossz(szelesseg,hosszusag,magassag):
    terfogat=szelesseg*hosszusag*magassag/1000
    return terfogat

szelesseg=int(input("Kérem, adja meg az akvárium szélességét egész centiméterben:"))        
hosszusag=int(input("Kérem, adja meg az akvárium hosszúságát egész centiméterben:"))  
magassag=int(input("Kérem, adja meg az akvárium magasságát egész centiméterben:"))

print(f"Az akváriumban összesen {halHossz(szelesseg,hosszusag,magassag)} cm hal lehet")

for i in range(30,51,5):
    halakHossza=halHossz(50,70,i)
    halakSzama=halakHossza//3
    print(f"Ha a magasság {i} cm akkor {round(halakSzama)} db hal telepíthető")

i=1
tovabb=True
while (tovabb):
    if (halHossz(i,80,35)>=160):
        tovabb=False
        print(f"A szélességnek minimum {i} cm-nek kell lennie.")
    
    i+=1

    









