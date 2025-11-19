# Innledning
print("Velkommen til prosjekt-simulatoren!")
print("Du spiller som Erling, prosjektleder for utviklingen av kommunens nye medborgerportal.\n")

# ---------------------------------------------------------------------
# BESLUTNINGSPUNKT 1
print("Konflikten mellom Silje (designer) og Sivert (IT) øker.")
print("Hva gjør du?")
print("a aktivitet: Ta det opp i plenum")
print("b: Ha individuelle samtaler med dem")

valg1 = input("Skriv a eller b: ")

# ---------------------------------------------------------------------
# BESLUTNINGSPUNKT 2
print("\nDet er også spenning mellom Hamdi og Jabir.")
print("Hvordan håndterer du dette?")
print("a: Ta et felles møte for avklaringer")
print("b: Avvente og håpe de finner ut av det selv")

valg2 = input("Skriv a eller b: ")

# ---------------------------------------------------------------------
# BESLUTNINGSPUNKT 3
print("\nTeamets motivasjon faller.")
print("Hva gjør du?")
print("a: Prioritere relasjonsbygging (sosial aktivitet)")
print("b: Prioritere fremdrift og leveranser")

valg3 = input("Skriv a eller b: ")

# ---------------------------------------------------------------------
# ENDEPUNKTER BASERT PÅ VALG

print("\n SLUTTRESULTAT")

# Her lager vi tre mulige endepunkter
# Dere kan endre tekstene så de passer til deres storyline

if valg1 == "a" and valg2 == "a" and valg3 == "a":
    print("Teamet gjenoppretter tillit og går videre til norming-fasen!")
elif valg3 == "b" and (valg1 == "b" or valg2 == "b"):
    print("Konfliktene løses delvis, men relasjonene forblir sårbare.")
else:
    print("Prosjektet mister samhold og blir forsinket.")
