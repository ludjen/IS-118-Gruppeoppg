def velg():
    valg = input("Ditt valg (A/B): ").upper()
    while valg not in ("A", "B"):
        valg = input("Skriv A eller B: ").upper()
    return valg

# Første beslutning
print("\nSituasjon 1: Konflikt mellom Silje og Sivert")
print("A) Ta det opp i plenum")
print("B) Ta individuelle samtaler")
valg1 = velg()

# Andre beslutning
print("\nSituasjon 2: Konflikt mellom Hamdi og Jabir")
print("A) Felles møte")
print("B) Avvente og håpe partene finner løsning selv")
valg2 = velg()

# Tredje beslutning
print("\nSituasjon 3: Motivere teamet")
print("A) Relasjonsbygging / sosiale aktiviteter")
print("B) Fokus på fremdrift og leveranser")
valg3 = velg()

# Resultat
print("\n=== Dine valg gir dette resultatet ===")

if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("Du valgte åpenhet hele veien. God tillit, men konflikter kan ta tid.")
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("Du valgte lukkede løsninger. Rask fremdrift, men lavere motivasjon.")
elif valg3 == "A":
    print("Du valgte relasjonsbygging. Teamet får god stemning og samhold.")
else:
    print("Du blandet åpne og lukkede valg. Teamet finner en god balanse.")

print("\nTakk for at du spilte! 🎉")
