from abc import ABC, abstractmethod


class Curavel(ABC):
    @abstractmethod
    def receber_cura(self, quantidade):
        pass


class Equipavel(ABC):
    @abstractmethod
    def equipar(self, arma):
        pass

    @abstractmethod
    def desequipar(self):
        pass