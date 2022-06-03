from bangunruang import PenghitungBangunRuang

class Kubus(PenghitungBangunRuang):

    def __init__(self, sisi : float):
        super().__init__(sisi)

    def hitung_keliling(self):
        print("Hasil Keliling Kubus : ",self.get_sisi()*12)

    def hitung_luas(self):
        print("Hasil luas Kubus : ",self.get_sisi()*self.get_sisi()*6)
        
    def hitung_volume(self):
        print("Hasil volume Kubus : ",self.get_sisi()*self.get_sisi()*self.get_sisi())