

class Clovek():

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
    
    def __str__(self):
        return(
            "Jméno pojistence: " + self.jmeno + "\n" + 
            "Příjmeni pojištěnce: " + self.prijmeni + "\n" + 
            "Věk pojištěnce: " + self.vek + "\n" + 
            "Telefonní číslo pojištěnce: " + self.telefon + "\n"  
        )