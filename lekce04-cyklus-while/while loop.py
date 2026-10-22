#heslo = input("Zadat heslo: ")
#while heslo != "pyladies":
#    print ("neprihhlasena")
#    heslo = input("zadat heslo znovu: ")
#print("vitej")

from random import randrange


hod = randrange (1,7)
while hod !=  6:
    print("Padlo", hod, "hazime znovu")
    hod = randrange (1,7)
    if hod ==1:
        print("koncime")
print ("padla", hod, "vyhrála si")