# Bonus 2 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Průměr od 1 do N. Uživatel zadá číslo N. Vypiš průměr všech čísel
#     od 1 do N (součet čísel vyděl jejich počtem).


N = int(input("zadej číslo N:"))
print(sum(range(1,N+1)) /len(range(1,N+1)))