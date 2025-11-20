
# Hvordan skal Erling løse konfliktene han står overfor på jobben?

# Første valget til Erling

print("Velkommen til Erling's konfliktløsningsprogram!")

print("Du spiller som Erling og står overfor en konflikt på jobben. hvordan vil du løse det?")

def pause():
    input("Trykk Enter for å fortsette...")

pause()

print("Silje og Sivert er uenige om hvordan de skal løse et prosjekt.")


print("Hvordan vil du håndtere konflikten mellom Silje og Sivert?\n")

print("a: Ta det opp med hele teamet for å få flere perspektiver.\n b: Snakke direkte med Silje og Sivert for å forstå deres synspunkter.")

choice1 = input()

if choice1 == "a":
    print("Du valgte å ta det opp med hele teamet.")
    print("Teamet gir verdifulle innspill, og dere finner en løsning sammen.")
elif choice1 == "b":
    print("Du valgte å snakke direkte med Silje og Sivert.")
    print("Gjennom samtalen forstår du deres synspunkter bedre, og de blir enige om en løsning, men du gikk glipp av andre perspektiver fra teamet.")

pause()

print("Det har også oppstått en konflikt mellom Hamdi og Jabir som du må håndtere.\n")
pause()
print("Hvordan vil du håndtere konflikten mellom Hamdi og Jabir?\n")

print("a: Inkalle til et felles møte for avklaring om hva som har skjedd. \n b: Vente og håpe at de finner ut av en løsning på egenhånd.")

choice2 = input()

if choice2 == "a":
    print("Du valgte å inkalle til et felles møte.")
    print("Møtet fører til en åpen dialog, og Hamdi og Jabir finner en løsning sammen.")
elif choice2 == "b":
    print("Du valgte å vente og håpe de finner ut av det selv.")
    print("Konflikten eskalerer, og det påvirker teamets moral negativt.")

pause()

print("Nå har du løst to konflikter, og det er bare en ting til å gjøre.\n Du må følge opp med teamet ditt for å sikre at alle er fornøyde langsiktig.\n")

pause()

print("Hvordan vil du holde oppe motivasjonen i teamet ditt i lengden?\n")

print("a: Arrangere sosiale aktiviteter og gi tid til å styrke samhold og tillitt i teamet. \n b: Fokusere på prestasjoner og resultater.")
choice3 = input()

if choice3 == "a":
    print("Du valgte å arrangere sosiale aktiviteter.")
    print("Teamet føler seg mer sammensveiset og motivert, noe som fører til bedre samarbeid og resultater.")
elif choice3 == "b":
    print("Du valgte å fokusere på prestasjoner og resultater.")
    print("Selv om teamet leverer gode resultater, føler noen seg oversett og det preger arbeidsmoralen i teamet.")

pause()

if (choice1 == "a" and choice2 == "a" and choice3 == "a"):
    print("Gratulerer! Du har håndtert konfliktene på en utmerket måte og skapt et sterkt og motivert team!")
elif (choice1 == "b" and choice2 == "b" and choice3 == "b"):
    print("Konflikthåndtering er ikke din sterkeste siden, men du er sikkert god på andre ting!")
else:
    print("Du har gjort ditt beste, men det er fortsatt rom for forbedering i konflikthåndtering og teamledelse. Lykke til videre!")

    
    
