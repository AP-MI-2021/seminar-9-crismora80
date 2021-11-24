from dataclasses import dataclass

from Domain.entity import Entity

@dataclass
class Ruta(Entity):
    idOrasPornire: str
    idOrasOprire: str
    pret: float
    dusIntors: bool