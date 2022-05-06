from datetime import date
from Impuesto import Impuesto
from Impuestos import Impuestos


iva_superreducido_anterios =Impuesto(
    1,'IVA superreducido',4.0,date(2010,7,1),date(2012,8,31)
)

iva_normal_anterior=Impuesto(
    2,'IVA normal',18.0,date(2010,7,1),date(2012,8,31)
)

iva_superreducido_actual= Impuesto(
    3,'IVA superreducido',4.0,date(2012,9,1)
)

iva_normal_actual=Impuesto(4,'IVA normal',21.0,date(2012,9,1))

print(iva_superreducido_anterios)
print(iva_normal_anterior)
print(iva_superreducido_actual.valor)
print(iva_normal_actual.valor)

impuestos=Impuestos()
impuestos.añadir(iva_superreducido_anterios)
impuestos.añadir(iva_normal_anterior)
impuestos.añadir(iva_superreducido_actual)
impuestos.añadir(iva_normal_actual)

print(impuestos)
print(impuestos.recuperar(3))
print(impuestos.recuperar(4))
print(impuestos.recuperarTodos)