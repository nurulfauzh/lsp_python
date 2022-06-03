from bangundatar import PenghitungBangunDatar

class Persegi(PenghitungBangunDatar):

    def __init__(self, sisi: float):
        super().__init__(sisi)
        
    def hitung_luas(self):
        luas = self.get_sisi() * self.get_sisi()
        print("Hasil Luas Persegi : ",luas)

    def hitung_keliling(self):
        print("Hasil Keliling Persegi : ", self.get_sisi()*4) 