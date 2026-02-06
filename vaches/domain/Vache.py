from typing import Any
from vaches.Exception import InvalidVacheException

class Vache:
    # Constantes
    AGE_MAX = 25
    POIDS_MAX = 1200.0
    PANSE_MAX = 200.0
    RENDEMENT_RUMINATION = 0.25

    def __init__(self, petit_nom: str, poids: float, age: int, panse: float = 0.0):
        # Validation
        self._valider_etat_initial(petit_nom, poids, age)

        self._petit_nom = petit_nom
        self._poids = float(poids)
        self._age = int(age)
        self._panse = float(panse)


    @property
    def petit_nom(self) -> str:
        return self._petit_nom

    @property
    def poids(self) -> float:
        return self._poids

    @property
    def age(self) -> int:
        return self._age

    @property
    def panse(self) -> float:
        return self._panse

    # --- Méthodes Métier ---

    def _valider_etat_initial(self, petit_nom: str, poids: float, age: int):
        if not petit_nom or not petit_nom.strip():
            raise InvalidVacheException("Le petit nom ne peut pas être vide.")
        if not (0 <= age <= self.AGE_MAX):
            raise InvalidVacheException(f"L'âge doit être compris entre 0 et {self.AGE_MAX}.")
        if poids < 0:
            raise InvalidVacheException("Le poids doit être positif.")

    def brouter(self, quantite: float, nourriture: Any = None):
        if nourriture is not None:
            raise InvalidVacheException("Une vache standard ne peut pas sélectionner sa nourriture.")
        if quantite <= 0:
            raise InvalidVacheException("La quantité broutée doit être strictement positive.")
        if self._panse + quantite > self.PANSE_MAX:
            raise InvalidVacheException(f"Capacité de la panse dépassée ({self.PANSE_MAX} kg max).")
        self._panse += quantite

    def ruminer(self) -> None:
        if self._panse <= 0:
            raise InvalidVacheException("Impossible de ruminer avec la panse vide.")

        panse_avant = self._panse

        # Gain de poids
        gain = self.RENDEMENT_RUMINATION * panse_avant
        self._poids += gain

        # Hooks (Template Method)
        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)
        self._post_rumination(panse_avant, lait)

        # Vider la panse
        self._panse = 0.0

    def vieillir(self) -> None:
        if self._age >= self.AGE_MAX:
            raise InvalidVacheException("La vache a atteint son âge limite.")
        self._age += 1

    def __str__(self) -> str:
        return f"Vache {self._petit_nom} (Age: {self._age}, Poids: {self._poids}kg)"

    # --- Hooks ---
    def _calculer_lait(self, panse_avant: float) -> float:
        return 0.0

    def _stocker_lait(self, lait: float) -> None:
        pass

    def _post_rumination(self, panse_avant: float, lait: float) -> None:
        pass