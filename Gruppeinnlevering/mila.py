def pause():
    input("Trykk Enter for å fortsette...")

print("Velkommen til Erling sitt konfliktspill!")
print("Du spiller som Erling, prosjektleder for en digital medborgerportal.")
pause()

print("Nå må du ta et valg i en konflikt mellom Silje og Sivert.\n")
pause()

print("Silje og Sivert er uenige om teknologivalg og design.")
print("Du må velge hvordan du vil håndtere konflikten.\n")
pause()

print("Hva vil du gjøre?")
print("a: Ta konflikten opp i plenum med hele teamet.")
print("b: Ta individuelle samtaler med Silje og Sivert.\n")

valg1 = input("Skriv a eller b og trykk Enter: ")

if valg1 == "a":
    print("\nDu tok konflikten opp i plenum.")
    print("Flere i teamet fikk si sin mening, men stemningen ble litt intens.")
elif valg1 == "b":
    print("\nDu tok individuelle samtaler med Silje og Sivert.")
    print("Temperaturen sank, men resten av teamet vet lite om hva som skjer.")
else:
    print("\nDu skrev ikke a eller b. Da blir konflikthåndteringen uklar.")

pause()
print("\nNå går vi videre til neste utfordring i prosjektet.")
print("En ny konflikt har oppstått mellom Hamdi og Jabir.")
pause()

print("Hamdi ønsker en kontrollert løsning for digitale folkemøter.")
print("Jabir ønsker en mer åpen dialogplattform.")
print("Du må velge hvordan du vil håndtere denne uenigheten.\n")
pause()
print("Hva vil du gjøre nå?")
print("a: Innkalle begge til et felles møte for avklaring.")
print("b: Avvente og håpe at de finner en løsning selv.\n")

valg2 = input("Skriv a eller b og trykk Enter: ")
if valg2 == "a":
    print("\nDu innkaller Hamdi og Jabir til et felles møte.")
    print("De får forklart sine synspunkter og finner et slags kompromiss.")
elif valg2 == "b":
    print("\nDu velger å avvente.")
    print("Konflikten vokser litt i det skjulte og skaper mer usikkerhet.")
else:
    print("\nDu skrev ikke a eller b. Konflikten forblir uløst.")
pause()

print("\nTil slutt må du tenke på motivasjonen i teamet.")
print("Etter konfliktene merker du at energien er lav, og fristen nærmer seg.")
pause()

print("Hvordan vil du jobbe med motivasjonen i teamet?\n")
print("a: Sette av tid til relasjonsbygging og sosiale aktiviteter.")
print("b: Prioritere fremdrift og resultater for å holde tempoet oppe.\n")

valg3 = input("Skriv a eller b og trykk Enter: ")

if valg3 == "a":
    print("\nDu setter av tid til relasjonsbygging.")
    print("Teamet får mer energi og føler sterkere samhold.")
elif valg3 == "b":
    print("\nDu prioriterer fremdrift og resultater.")
    print("Dere leverer raskt, men noen føler seg stresset og litt oversett.")
else:
    print("\nDu skrev ikke a eller b. Motivasjonen forblir uendret.")

pause()

# --- SLUTT PÅ HISTORIEN (3 mulige utfall) ---

# Vi teller gode valg (a = 1 poeng)
score = 0

if valg1 == "a":
    score += 1
if valg2 == "a":
    score += 1
if valg3 == "a":
    score += 1

print("\n--- SLUTTRESULTAT ---")

if score == 3:
    print("Utfall 1: Teamet gjenoppretter tillit og går inn i norming-fasen.")
    print("Alle konfliktene ble håndtert godt, og motivasjonen er høy!")
elif score == 2:
    print("Utfall 2: Konfliktene ble delvis løst.")
    print("Teamet fungerer, men relasjonene er fortsatt litt sårbare.")
else:
    print("Utfall 3: Prosjektet mister samhold.")
    print("Konfliktene hang igjen, motivasjonen sank, og prosjektet forsinkes.")

pause()
