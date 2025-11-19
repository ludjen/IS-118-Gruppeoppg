def pause():
    input("\n(trykk enter for å fortsette)\n")

print("Velkommen til 'Erling leder prosjektgruppen'!")

# Beslutningspunkt 1
print("\n Beslutningspunkt 1")
print("Silje og Sivert krangler om løsningene. Hva gjør du?")
print("a: Snakk med begge før felles møte")
print("b: La det gå, det er naturlig uenighet")
print("c: Ta avgjørelsen selv")

valg1 = input("Skriv a, b eller c: ")

# Beslutningspunkt 2
print("\n Beslutningspunkt 2")
print("Teamet er usikkert og går sakte fram. Hva gjør du?")

pause()

print("a: La gruppa planlegge selv")
print("b: Du lager en detaljert plan")
print("c: Hold en workshop for felles plan")

valg2 = input("Skriv a, b eller c: ")

# Beslutningspunkt 3
print("\n Beslutningspunkt 3")
print("Jabir og Hamdi bidrar lite. Hva gjør du?")
pause()
print("a: Ta en åpen runde med hele teamet")
print("b: Snakk med dem direkte")
print("c: Ignorer det og håp det ordner seg")

valg3 = input("Skriv a, b eller c: ")

# Avslutning basert på valg
print("\n Resultat")

if valg1 == "a" and valg2 == "c" and valg3 == "a":
    print("Du bygger et trygt og samarbeidsvillig team. Prosjektet lykkes!")
elif valg1 == "B" or valg2 == "B":
    print("Teamet føler seg lite involvert. Fremdriften blir treg.")
else:
    print("Teamet blir frustrert. Flere konflikter oppstår og prosjektet havner i trøbbel.")

