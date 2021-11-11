def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaator
    +-liitmine
    --lahutamine
    *-korrutamine
    /-jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Arimeetiline tehing
    :rtype float:"""
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c==":":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("viga")
    print(r)
    return r
def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigasta ja Flase kui ei ole
    :parem int aasta: Aasata number
    :rtype bool: Funksionid vastus loogilised formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vstus
def square(a: float,b:float,c:str):
    """
    see arvutab ruudu ümbermõõdu, ruudu pindala ja ruudu diagonaali.
    """
def season (kuu:int):
    if kuu==12:
      print("зима")
    elif 0<kuu<3:
        print("Зима")
    elif 2<kuu<6:
        print("весна")
    elif 5<kuu<9:
        print("Лето")
    elif 8<kuu<12:
        print("Осень")
    else:
        print("viga")
    return("")
def bank(a:float,years:int):
    for _ in range(years):
        a=((1.1*1/100)*a)*100
        print("Ваш баланс",a)
        return("")





   
    
