# Enkel interaktiv historie med pause
# Pause gjøres ved å vente på Enter, ikke time.sleep()

def pause():
    input("\nTrykk Enter for å fortsette...\n")

print("Velkommen til den interaktive historien!")
print("Du spiller som Erling, prosjektleder for et team med konflikter.\n")
pause()

# Første konflikt
print("Første konflikt: Silje og Sivert er uenige.")
print("a: Ta det opp i et møte med hele teamet.")
print("b: Snakke direkte med Silje og Sivert.")
choice1 = input("Skriv a eller b: ").lower()
pause()

if choice1 == "a":
    print("Teamet gir gode innspill, og dere finner en løsning sammen.\n")

elif choice1 == "b":
    print("Dere finner en løsning, men du mister teamets perspektiver.\n")
else:
    print("Ugyldig valg – vi antar du valgte b.\n")
    choice1 = "b"
pause()

# Andre konflikt
print("Ny konflikt: Hamdi og Jabir er uenige.")
print("a: Innkalle til et møte for å rydde opp.")
print("b: Vente og håpe de løser det selv.")
choice2 = input("Skriv a eller b: ").lower()
pause()

if choice2 == "a":
    print("Konflikten blir løst gjennom en åpen samtale.\n")
elif choice2 == "b":
    print("Konflikten eskalerer og påvirker teamets moral.\n")
else:
    print("Ugyldig valg – vi antar du valgte b.\n")
    choice2 = "b"
pause()

# Motivasjon
print("Hvordan vil du holde motivasjonen oppe i teamet?")
print("a: Arrangere sosiale aktiviteter.")
print("b: Fokusere på prestasjoner og resultater.")
choice3 = input("Skriv a eller b: ").lower()
pause()

if choice3 == "a":
    print("Teamet blir mer motivert og sammensveiset.\n")
elif choice3 == "b":
    print("Teamet leverer resultater, men noen føler seg oversett.\n")
else:
    print("Ugyldig valg – vi antar du valgte b.\n")
    choice3 = "b"
pause()

# Sluttresultat
print("=== SLUTTRESULTAT ===")
if choice1 == "a" and choice2 == "a" and choice3 == "a":
    print("Fantastisk! Du håndterte konfliktene perfekt og styrket teamet!")
elif choice2 == "b" and choice3 == "b":
    print("Teamet sliter, flere konflikter er uløst og prosjektet blir forsinket.")
else:
    print("Delvis suksess. Noe gikk bra, men det er rom for forbedring.")
pause()

print("\nTakk for at du spilte!")

