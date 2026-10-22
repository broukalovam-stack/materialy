# Cvičení 7 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počet sekund (třeba 3661). Přepočítej ho na hodiny,
#    minuty a sekundy a vypiš je jako 1:1:1 jediným printem.


cislo = int(input("Kolik sekund?"))
hodiny = (cislo//3600)
minuty = (cislo%3600//60)
sekundy= (cislo % 60)         
print(hodiny, minuty, sekundy, sep=":")