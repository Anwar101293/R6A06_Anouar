from vaches.InvalidVacheException import InvalidVacheException
class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1200.0
    PANSE_MAX = 200.0
    RENDEMENT_RUMINATION: float = 0.25
    petit_nom:str
    poids:float
    panse:float = 0.0
    age
    @property
    def petit_nom(self) -> str:
        return self._petit_nom

    @property
    def poids(self) -> float:
        return self._poids

    @property
    def age(self) -> float:
        return self._age

    @property
    def panse(self) -> float:
        return self._panse