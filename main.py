# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:53:51 2026

@author: HP
"""


from utils.top1 import musbatmi
from utils.top2 import juftmi
from utils.top3 import hisobla
from utils.top4 import orta
from utils.top5 import top
from utils.top6 import uzunlik
from utils.top7 import teskari
from utils.top8 import kuchlimi
from utils.top9 import filtr


while True:
    print("\nMENYU")
    print("1 musbat yoki manfiy")
    print("2 juft yoki toq")
    print("3 hisoblash")
    print("4 o‘rtacha qiymat")
    print("5 eng katta son")
    print("6 matn uzunligi")
    print("7 teskari matn")
    print("8 parol tekshir")
    print("9 musbat sonlar")
    print("0 hiqish")

    tanlov = input("Tanlov: ")

    if tanlov == "0":
        print("Dastur tugadi")
        break

    elif tanlov == "1":
        son = int(input("Son kiriting: "))
        print(musbatmi(son))

    elif tanlov == "2":
        son = int(input("Son kiriting: "))
        print(juftmi(son))

    elif tanlov == "3":
        a = float(input("a: "))
        b = float(input("b: "))
        amal = input("Amal (+ - * /): ")
        print(hisobla(a, b, amal))

    elif tanlov == "4":
        sonlar = list(map(int, input("Sonlar: ").split()))
        print(orta(sonlar))

    elif tanlov == "5":
        sonlar = list(map(int, input("Sonlar: ").split()))
        print(top(sonlar))

    elif tanlov == "6":
        matn = input("Matn: ")
        print(uzunlik(matn))

    elif tanlov == "7":
        matn = input("Matn: ")
        print(teskari(matn))

    elif tanlov == "8":
        parol = input("Parol: ")
        print(kuchlimi(parol))

    elif tanlov == "9":
        sonlar = list(map(int, input("Sonlar: ").split()))
        print(filtr(sonlar))

    

    else:
        print("Noto‘g‘ri tanlov!")