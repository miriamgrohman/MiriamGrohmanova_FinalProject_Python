from clovek import Clovek

class Evidence():
    def __init__(self):
        self.lidi = []

    def pridej(self,jmeno, prijmeni, vek, telefon):
        novy_clovek = Clovek(jmeno,prijmeni,vek,telefon)
        self.lidi.append(novy_clovek)

    def hledej(self,jmeno,prijmeni):
        nalezeno = False
        for clovek in self.lidi:
            if clovek.jmeno == jmeno and clovek.prijmeni == prijmeni:
                print(clovek)
                nalezeno = True
        if not nalezeno: 
            print("Pojištěnec nenalezen.")

    def tisk_vse(self):
        for clovek in self.lidi:
            print(clovek)