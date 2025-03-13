#-----------------------------------------------------------------------------------------------------------------------
 # Cabina de peaje 1.1 version GUI.
 # Castillo Maximo - 403257 - 1K10
#-----------------------------------------------------------------------------------------------------------------------
 # Ingreso de datos.
#-----------------------------------------------------------------------------------------------------------------------

import PySimpleGUI as psg

patente = psg.popup_get_text("Ingrese el numero de patente:")
tipo_de_vehiculo = int(psg.popup_get_text("Indique el tipo de vehiculo con un\n0) Para moto \n1) Para auto \n2) Para camion\n"))
metodo_de_pago = int(psg.popup_get_text("Indique la forma de pago:\n1) Manual\n2) Telepeaje\n"))
pais_ubicacion_peaje = int(psg.popup_get_text("Marque el pais en que se encuentra:\n0) Argentina\n1) Bolivia\n2) Brasil\n3) Paraguay\n4) Uruguay\n"))
distancia = float(psg.popup_get_text("Ingrese la distancia recorrida desde la ultima cabina de peaje, si es la primera marque 0:"))

#-----------------------------------------------------------------------------------------------------------------------
 # Variables fijas.
#-----------------------------------------------------------------------------------------------------------------------

importe_arg_par_uru = 300
importe_bra = 400
importe_bol = 200
descuento_telepeaje = 0.1
descuento_moto = 0.5
recargo_camion = 1.6

#-----------------------------------------------------------------------------------------------------------------------
 # Punto 1 (Indicar el país de procedencia del vehículo).
#-----------------------------------------------------------------------------------------------------------------------

if len(patente) >= 8:
    nacionalidad = "Otra (Su patente no corresponde al mercosur, contiene mas de siete caracteres)."
elif len(patente) <= 6:
    nacionalidad = "Otra (Su patente no corresponde al mercosur, contiene menos de siete caracteres)."
elif("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("0" <= patente[2] <= "9") and ("0" <= patente[3] <= "9") and ("0" <= patente[4] <= "9") and ("A" <= patente[5] <= "Z") and ("A" <= patente[6] <= "Z"):
    nacionalidad= "Argentina."
elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("0" <= patente[2] <= "9") and ("0" <= patente[3] <= "9") and ("0" <= patente[4] <= "9") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
    nacionalidad= "Boliviana."
elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("0" <= patente[3] <= "9") and ("A" <= patente[4] <= "Z") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
    nacionalidad = "Brasileña."
elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("A" <= patente[3] <= "Z") and ("0" <= patente[4] <= "9") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
    nacionalidad = "Paraguaya."
elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("0" <= patente[3] <= "9") and ("0" <= patente[4] <= "9") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
    nacionalidad = "Uruguaya."
elif len(patente) == 7:
    nacionalidad = "Otra (Su patente no corresponde al mercosur, formato desconocido)."

#-----------------------------------------------------------------------------------------------------------------------
 # Punto 2 (Indicar el importe básico a pagar por el vehículo).
#-----------------------------------------------------------------------------------------------------------------------

if pais_ubicacion_peaje == 0 :
    importe_sin_descuento = importe_arg_par_uru
elif  pais_ubicacion_peaje == 1:
    importe_sin_descuento = importe_bol
elif pais_ubicacion_peaje == 2:
    importe_sin_descuento = importe_bra
elif pais_ubicacion_peaje == 3:
    importe_sin_descuento = importe_arg_par_uru
elif pais_ubicacion_peaje == 4:
    importe_sin_descuento = importe_arg_par_uru


if pais_ubicacion_peaje == 0 :
    pais = "Argentina."
elif  pais_ubicacion_peaje == 1:
    pais = "Bolivia."
elif pais_ubicacion_peaje == 2:
    pais = "Brasil."
elif pais_ubicacion_peaje == 3:
    pais = "Paraguay."
elif pais_ubicacion_peaje == 4:
    pais = "Uruguay."


if tipo_de_vehiculo == 0:
    descuento_vehiculo = importe_sin_descuento * descuento_moto
elif tipo_de_vehiculo == 1:
    descuento_vehiculo = importe_sin_descuento
elif tipo_de_vehiculo == 2:
    descuento_vehiculo = importe_sin_descuento * recargo_camion


if tipo_de_vehiculo == 0:
    vehiculo= "Moto"
elif tipo_de_vehiculo == 1:
    vehiculo= "Automóvil"
elif tipo_de_vehiculo == 2:
    vehiculo= "Camión"

#-----------------------------------------------------------------------------------------------------------------------
 # Punto 3 (Si la forma de pago fue por telepeaje se aplica un descuento del 10%).
#-----------------------------------------------------------------------------------------------------------------------

if metodo_de_pago == 1:
    telepeaje= descuento_vehiculo
elif metodo_de_pago == 2:
    telepeaje= descuento_vehiculo * descuento_telepeaje

#-----------------------------------------------------------------------------------------------------------------------
 # Punto 4 (Valor promedio pagado por ese vehículo por cada kilómetro recorrido desde la última cabina).
#-----------------------------------------------------------------------------------------------------------------------

if telepeaje == descuento_vehiculo:
    monto_total= descuento_vehiculo
else:
    monto_total= descuento_vehiculo - telepeaje


if distancia == 0:
    valor_promedio = "=> Usted esta en su primer peaje, por lo tanto no se calcula el promedio de kilómetros pagados."
else:
    valor_promedio = "=> El valor promedio pagado por " + str(distancia) +"  kilómetros recorridos desde la última cabina es de: " + str(round(monto_total / distancia , 2)) + " $ARS."

#-----------------------------------------------------------------------------------------------------------------------
 # Correccion para el punto 3
# -----------------------------------------------------------------------------------------------------------------------

if telepeaje == descuento_vehiculo:
    telepeaje = "=> La forma de pago por manual no aplica para recibir el descuento del 10%."
else:
    telepeaje= "=> El descuento por usar telepeaje es de: " + str(telepeaje) + " $ ARS."


#-----------------------------------------------------------------------------------------------------------------------
# Ticket
#-----------------------------------------------------------------------------------------------------------------------

n1= "------------ Bienvenido al peaje de: " + pais + " ------------"
n2= "* Patente: " + patente
n3= "* Procedencia del vehiculo: " + nacionalidad
n4= "* Tipo de vehiculo: " + vehiculo + "."
n5= "=> El importe a pagar por: "  + vehiculo + " es de: " + str(descuento_vehiculo) + " $ ARS."
n6= telepeaje
n7= "=> Total a pagar: " + str(monto_total) + " $ ARS."
n8= valor_promedio
n0= "            "
psg.popup_scrolled(n1,n0,n2,n0,n3,n0,n4,n0,n5,n0,n6,n0,n7,n0,n8 ,title="Ticket: Cabina de peaje.")
