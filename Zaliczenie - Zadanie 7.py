class Samochod:

    def __init__(self, marka, model, rok_produkcji, przebieg) :
        self.marka = marka if isinstance(marka, str) else ""
        self.model = model if isinstance(model, str) else ""
        self.rok_produkcji = rok_produkcji if isinstance(rok_produkcji, int) else 0
        self.przebieg = przebieg if isinstance(przebieg, float) else 0.0
    

    def __str__(self):
        return f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}, Przebieg: {self.przebieg:.2f} km"

        

    def __lt__(self, other):
        
        if self.przebieg < other.przebieg:
            return True
        else:
            return False
       
        
samochod1 = Samochod("Opel","Astra G", 1999, 220000.537)   
    
samochod2 = Samochod("Opel","Astra G", 2000, 280000.891)   

print(samochod1)
print("---------------------------------------------------------------------------------------")
print(samochod2)
print("---------------------------------------------------------------------------------------")
print(samochod1 < samochod2)