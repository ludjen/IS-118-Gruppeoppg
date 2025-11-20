#denne sørger for at input alltid er a eller b
#dersom input er noe annet vil koden fortsette å spørre etter svar.

def get_choice(questions):
    while True:   
        svar = input(questions + " (a/b): ").strip().lower()
        if svar in ("a", "b"):
            return svar
        print("Ugyldig valg, svar a eller b.")

#Her lagde jeg en pause, slik at bruker får tid til å lese, uten at det blir rotete.

def pause():
    input("\n(Trykk Enter for å fortsette)\n")


def spill():
    print("\n Prosjektleder Erling sin Interaktive historie \n")
    print("Du leder et prosjekt for kommunens nye digitale medborgerportal.")
    print("Det er spenninger i teamet, og du må ta tre viktige valg.")
    pause()


#her gir jeg brukeren sitt første valg og kaller derfor på get_choice.
    
    print("BESLUTNING 1, Konflikt mellom Silje (UX) og Sivert (IT)\n")
    print("a) Ta det opp i plenum for å skape åpenhet")
    print("b) Ta individuelle samtaler for å dempe temperaturen")
    c1 = get_choice("Hva gjør du?")
    if c1 == "a":
        print("\nDu tar saken i plenum. Konflikten blir synlig, flere synspunkter kommer fram.")
    else:
        print("\nDu tar individuelle samtaler. Du demper temperaturen og får bedre innsikt i motivene.")
    pause()

    
    print("BESLUTNING 2, Uenighet mellom Hamdi (kultur) og Jabir (brukerrep)\n")
    print("a) Kalle inn til felles møte for avklaring")
    print("b) Avvente og håpe de finner en løsning selv")
    c2 = get_choice("Hva gjør du?")
    if c2 == "a":
        print("\nDu kaller inn til et strukturert møte med tydelig avklaring.")
    else:
        print("\nDu avventer. De får prøve å løse det selv.")
    pause()

    
    print("BESLUTNING 3, Motivasjon i teamet\n")
    print("a) Sette av tid til relasjonsbygging og sosiale aktiviteter")
    print("b) Prioritere fremdrift og leveranser")
    c3 = get_choice("Hva gjør du?")
    if c3 == "a":
        print("\nDu prioriterer relasjoner. Teamet får puste og bygge tillit.")
    else:
        print("\nDu presser på for fremdrift. Det gir progresjon, men kan slite på enkelte.")
    pause()

    #liten oppsummering som avhenger av brukerens valg.
    print("\n Oppsummering av valg")
    print("1) Silje/Sivert: ", "Plenum" if c1 == "a" else "Samtaler")
    print("2) Hamdi/Jabir: ", "Felles møte" if c2 == "a" else "Avvente")
    print("3) Motivasjon:  ", "Relasjoner" if c3 == "a" else "Fremdrift")
    pause()

    #her får bruker sitt resultat avhengig av hvordan de har svart på tidligere valg.

    print("\n RESULTAT \n")
    if c1 == "a" and c2 == "a" and c3 == "a":
        print("Teamet gjenoppretter tillit og går inn i norming-fasen.")
        print("Prototype leveres i tide, og teamet fungerer godt videre.")
    elif c1 == "b" and c2 == "b" and c3 == "b":
        print("Prosjektet mister samhold og blir forsinket.")
        print("Misnøye vokser under overflaten, og det kan trenges ekstern hjelp.")
    else:
        print("Konfliktene løses delvis, men relasjonene er sårbare.")
        print("Prosjektet fortsetter, men med risiko for nye gnister.")

    print("\nTakk for at du spilte gjennom scenarioet!")

spill()

