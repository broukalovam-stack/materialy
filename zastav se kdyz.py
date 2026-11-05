""" def prihlaseni (jmeno, heslo):
    jmeno = input("Zadej jmeno")
    helso = input("zadej heslo")
    if len(heslo)>8:
        print ("Vítej, jmeno")
    else:
        print("Heslo neni dostatečne dlouhé") """


def je_heslo_dlouhe(heslo):
    #return len(heslo) >8
#take to můze byt pres if něco return True, else return False
    if len(heslo)>8:
        return False
    elif len(heslo)< 15:
        return False
    else:
        return True

def zeptej_se_na_jmeno():
    jmeno = input("zadej jmeno")
    # uprava jmeno
    return jmeno     

def zeptej_se_na_heslo():
    return input ("zadej heslo")   

def prihlaseni ():
    jmeno = input("Zadej jmeno")
    heslo = input("zadej heslo")
    if je_heslo_dlouhe(heslo):
        print("vítej", jmeno)
    else:
        print("Heslo ma spatnou delsku")

prihlaseni ("Tomas","1")



#řešení od Barci
def je_heslo_dlouhe(heslo):
    if len(heslo) < 8:
        False
    else:
        return True

def zeptej_se_na_jmeno():
    jmeno = input("Zadej jmeno: ")
    return jmeno

def zeptej_se_na_heslo():
    return input("Vložte heslo: ")
    
def prihlaseni():
    jmeno = zeptej_se_na_jmeno()   
    heslo = zeptej_se_na_heslo()
    if je_heslo_dlouhe(heslo):
        print("Vítej", jmeno)
    else:
        print("Heslo má špatnou délku.")
        
    
prihlaseni()