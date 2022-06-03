from abc import ABC , abstractmethod

class PenghitungBangunDatar(ABC):
    
    def __init__(self,sisi : float):
        self.__sisi= sisi
    def get_sisi(self):
        return self.__sisi

    @abstractmethod
    def hitung_keliling():
        pass
    @abstractmethod
    def hitung_luas():
        pass 