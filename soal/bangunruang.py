from abc import ABC , abstractmethod

class PenghitungBangunRuang(ABC):

    def __init__(self, sisi : float):
        self.__sisi= sisi
        
    def get_sisi(self):
        return self.__sisi

    @abstractmethod
    def hitung_keliling():
        pass
    def hitung_volume():
        pass
    def hitung_luas():
        pass 