
from Impuesto import Impuesto
from dataclasses import dataclass


@dataclass
class Impuestos:
    def __init__(self):
        self.impuestos: list[Impuesto] = []

    def recuperarTodos(self) -> list[Impuesto]:
        return self.impuestos
    def añadir(self,impuesto: Impuesto) -> None:
        self.impuestos.append(impuesto)

    def recuperar(self,impuestoId:Impuesto) -> Impuesto:
        for impuesto in self.impuestos:
            if impuesto.id == impuestoId:
                return impuesto
        raise Exception(f'No existe el impuesto con id {impuestoId}')

    def __repr__(self) -> str:
        cadena= 'IMPUESTO'
        for impuesto in self.impuestos:
            cadena += '\n\t'+ impuesto.__repr__()
            return cadena