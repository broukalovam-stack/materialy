for cislo in range (1,11):
    print("Aktualni cislo je: ", cislo)

#chceme se zbavit duplikace dáme si range do proměné
max_hodnota = 10

# for cislo in range (1,max_hodnota)  #max hodnota 10
#     print  print("Aktualni cislo je: ", cislo)

# for cislo in range (1,max_hodnota) #max hodnota 100
#     print  print("Aktualni cislo je: ", cislo)

# for cislo in range (1,max_hodnota)#max hodnota 1000
#     print  print("Aktualni cislo je: ", cislo)

#definujeme si funkce
# def vypis_cisla_do_max_hodnoty(max_hodnota):
#     for aktualni_cislo in range (1,max_hodnota):
#         print(aktualni_cislo)


# # vypis_cisla_do_max_hodnoty(max_hodnota)
# vypis_cisla_do_max_hodnoty(10)
# vypis_cisla_do_max_hodnoty(100)
# vypis_cisla_do_max_hodnoty(1000)

# def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani):
#     for aktualni_cislo in range (1,max_hodnota):
#         print(jmeno_volani,":",aktualni_cislo)


# # vypis_cisla_do_max_hodnoty(max_hodnota)
# vypis_cisla_do_max_hodnoty(10, "Volani A")
# print("-"*30)
# vypis_cisla_do_max_hodnoty(100, "Volani B")
# print("-"*30)
# vypis_cisla_do_max_hodnoty(1000, "Volani C")
# print("-"*30)

# def vypis_cisla_do_max_hodnoty(max_hodnota, jmeno_volani):
#     for aktualni_cislo in range (1,max_hodnota):
#         print(jmeno_volani,":",aktualni_cislo)
#     print("-"*30)


# # vypis_cisla_do_max_hodnoty(max_hodnota)
# vypis_cisla_do_max_hodnoty(10, "Volani A")
# vypis_cisla_do_max_hodnoty(100, "Volani B")
# vypis_cisla_do_max_hodnoty(1000, "Volani C")
""" 
def vypis_cisla_do_max_hodnoty (max_hodnota, jmeno_volani, ukaz_caru):
    for aktualni_cislo in range (1,max_hodnota):
        print(jmeno_volani,":"+ str(aktualni_cislo))
    if ukaz_caru:
        print("-"*30)


# vypis_cisla_do_max_hodnoty(max_hodnota)
vypis_cisla_do_max_hodnoty (10, "Volani A", True)
vypis_cisla_do_max_hodnoty (100, "Volani B", True)
vypis_cisla_do_max_hodnoty (1000, "Volani C", False) """



def vypis_cisla_do_max_hodnoty (max_hodnota, jmeno_volani, ukaz_caru = True):#díky tomu, ze ji tady mám definovanou, takže pak tam můžu dát pak jen dva parametry,
    # a ten třetí jen když nechci true a vždy to musí být nakonci... mohou být definovanž i víc třeba jemno_volani = A a pak tam můzu mit jen jednu dokud to nechci změnit
    for aktualni_cislo in range (1,max_hodnota):
        print(jmeno_volani,":"+ str(aktualni_cislo))
    if ukaz_caru:
        print("-"*30)


# vypis_cisla_do_max_hodnoty(max_hodnota)
vypis_cisla_do_max_hodnoty (10, "Volani A")
vypis_cisla_do_max_hodnoty (100, "Volani B")
vypis_cisla_do_max_hodnoty (1000, "Volani C", False)


# def cena_mhd(vek):
#     print("Pocitam cenu listku pro vek", vek)

#     if vek <6:
#         print ("Cena 0")
#     elif vek <18:
#         print ("Cena 39")
#     elif vek <65:
#         print ("Cena 50")
#     else:
#          print ("Cena 0")
# cena_mhd(11)

def cena_mhd(vek):
    print("Pocitam cenu listku pro vek", vek)

    if vek <6:
        return 0
    elif vek <18:
        return 39
    elif vek <65:
        return 50
    else:
         return 0
    
zustatek_uctu = 100
cena_jizdenky = cena_mhd(7)
print("Výsledná cena je:", cena_jizdenky)
zustatek_uctu = zustatek_uctu - cena_jizdenky