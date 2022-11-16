from evidence import Evidence

ev = Evidence()
jede = True
while jede:
    prikaz = input("Co chceš dělat? \n\n 1 = přidej človeka do evidence \n 2 = vyhledej človeka v evidenci \n 3 = vytiskni celou evidenci \n 4 = konec \n\n Zde napiš svoji volbu: ")
    if prikaz == "1":
        jmeno = input("Zadej jméno: ")
        prijmeni = input("Zadej příjmení: ")
        vek = input("Zadej věk: ")
        telefon = input("Zadej telefonní číslo: ")
        ev.pridej(jmeno, prijmeni, vek, telefon)
    elif prikaz == "2":
        jmeno = input("Zadej jméno: ")
        prijmeni = input("Zadej příjmení: ")
        ev.hledej(jmeno, prijmeni)
    elif prikaz == "3":
        ev.tisk_vse()
    elif prikaz == "4":
        jede = False
        print("Tak to pochop už je konec...")
        print("Ztratíš vsechna data..")
    else:
        print("Špatný příkaz, zkus to znovu, třeba ti to jednou vyjde.")
            
