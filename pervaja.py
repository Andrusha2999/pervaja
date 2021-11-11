from module1 import *
while True:
    print("funksioind".center(50,"+"))
    print("arithmetic- A,\nis_year_leap-Y,\nseason- D ,\nyears- V")
    v=input("arithmetic- A")
    if v.upper()=="A":
        a=float(input("esimene arv"))
        b=float(input("teine arv"))
        sym=input("Tehe:")
        result=arithmetic(a,b,sym)
        print(rezult)
    elif v.upper()=="Y":
        is_year_leap()
        result=is_year_leap((int(input("sisesta aasta"))))
    elif v.upper()=="D":
        a=int(input("sisestage kuu"))
        result=Aastahad(a)
        print(result)
    



        