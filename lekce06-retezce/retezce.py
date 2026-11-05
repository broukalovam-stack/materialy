""" # vek = int(input("Zadej svůj vek: "))
# print ("Za 10 let ti bude", vek +10)


vek = input("Zadej svůj vek: ")
print (vek *4)
print ("Za 10 let ti bude",int(vek) +10)

print(len(vek))

if "0" in vek:
   print("Tvuj vek konci nulou")
else:
    print("Tvuj vek nekoneci nulou")
 """
#for pismeno in jmeno:
    #print(jmeno)


vek = 30
jmeno = "Anna"
print(f"Jsem {jmeno} a je mi {vek}")

kniha = "Maly princ"
stran_celkem = 320
precteno = 120
print(f"V {kniha} zbyvá {stran_celkem-precteno} stranek do konce")


def procenta(cast, celek):
    return cast/celek*100

print(f"Mas precteno {procenta(precteno, stran_celkem):.2f} procent knihy")

#\n new line (za to za co to dáš tak to pak skočí na nový řádek)
#\t tap (tabulator)
#\"Tomas\" kdyz chci dát text do uzovek
# nebo taky můu použít v textu ty druhé uvozovky, které jsem nepouzila na to definování si textu
#\\ tomas\\ takhle dám do textu jedno vec do lomitek
#""" text""" formátuje se to podle toho co tam zadám, takže mezery entry, odsazení


print("pyladies".upper())

print("Ahoj Adame"lower().count("a"))



def zeptat_se_na_email():
    return input("Napis sem email:").lower()

Jmv


vek = input("Zadej vek: ")
if vek.isdigit():
    print("Za 10 let ti bude", int(vek)+10)
else:
    print("Pises blbosti, jdi pryc")