# Bonus 1 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.

CelkovaUtrata = int(input("Kolik byla útrata?"))
PocetLidi = int(input("Kolik bylo lidi?"))
print(round(CelkovaUtrata/PocetLidi,2))
