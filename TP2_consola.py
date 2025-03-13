#-----------------------------------------------------------------------------------------------------------------------
 # Cabina de peaje 2.0
 # Castillo Maximo - 403257 - 1K10
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
 # Funciones a utilizar.
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
 # Con esta funcion obtendremos el importe final.
#-----------------------------------------------------------------------------------------------------------------------
def obtener_importe_final(tipo_vehiculo , pais_de_cabina , forma_pago):
    importe_arg_par_uru = 300
    importe_bra = 400
    importe_bol = 200
    descuento_telepeaje = 0.1
    descuento_moto = 0.5
    recargo_camion = 1.6

    if pais_de_cabina == 0:
        importe_sin_descuento = importe_arg_par_uru
    elif pais_de_cabina == 1:
        importe_sin_descuento = importe_bol
    elif pais_de_cabina == 2:
        importe_sin_descuento = importe_bra
    elif pais_de_cabina == 3:
        importe_sin_descuento = importe_arg_par_uru
    elif pais_de_cabina == 4:
        importe_sin_descuento = importe_arg_par_uru


    if tipo_vehiculo == 0:
        descuento_vehiculo = importe_sin_descuento * descuento_moto
    elif tipo_vehiculo == 1:
        descuento_vehiculo = importe_sin_descuento
    elif tipo_vehiculo == 2:
        descuento_vehiculo = importe_sin_descuento * recargo_camion

    if forma_pago == 1:
        telepeaje= descuento_vehiculo
        return int(telepeaje)
    elif forma_pago == 2:
        telepeaje= descuento_vehiculo - (descuento_vehiculo * descuento_telepeaje)
        return int(telepeaje)

#-----------------------------------------------------------------------------------------------------------------------
 # Con esta funcion obtendremos el porcentaje redondeado a no más de dos decimales que representa la cantidad de patentes de
 # otros países sobre el total de patentes procesadas (es 1(un) resultado de tipo float: el porcentaje redondeado a no más de dos decimales).
# ----------------------------------------------------------------------------------------------------------------------
def calculo_de_porcentaje(carg , cbol , cbra , cchi , cpar , curu , cotr):
    porc = 0
    suma = carg + cbol + cbra + cchi + cpar + curu + cotr
    if suma > 0:
        porc = cotr * 100 / suma
    return round(porc, 2)

#-----------------------------------------------------------------------------------------------------------------------
 # Con esta funcion obtendremos el idioma en el que se espera que los empleados de la empresa generen los reportes: Portugués o Español.
 # Se aceptarán como válidas solamente las palabras “Español” (con ñ) o “Portugués” (con acento en la é), en cualquier combinación de minúsculas o mayúsculas.
# ----------------------------------------------------------------------------------------------------------------------
def obtener_idioma(linea):
    if ' PT ' in linea or ' PT' in linea or 'PT ' in linea:
        return 'Portugués'
    elif ' ES ' in linea or ' ES' in linea or 'ES ' in linea:
        return 'Español'

# -----------------------------------------------------------------------------------------------------------------------
 # Con esta funcion obtendremos la distancia promedio redondeada a no más de dos decimales recorrida por los vehículos con
 # patente de Argentina que pasaron por cabinas brasileñas.
# ----------------------------------------------------------------------------------------------------------------------
def calculo_de_kilometros(v1 , v2 ):
    prom = kilometros_argentina / paso_por_brasil
    return round(prom, 2)

# -----------------------------------------------------------------------------------------------------------------------
 # Con esta funcion obtendremos el pais de orgen del vehiculo.
 # Usaremos el mismo algoritmo utilizado en el TP1.
# ----------------------------------------------------------------------------------------------------------------------
def detector_de_pais(patente):
    if len(patente) >= 8:
        return 'cotr' #"Otra (Su patente no corresponde al mercosur, contiene mas de siete caracteres)."
    elif len(patente) <= 6:
        return 'cotr' #"Otra (Su patente no corresponde al mercosur, contiene menos de siete caracteres)."
    elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("0" <= patente[2] <= "9") and ("0" <= patente[3] <= "9") and ("0" <= patente[4] <= "9") and ("A" <= patente[5] <= "Z") and ("A" <= patente[6] <= "Z"):
        return 'carg' #"Argentina."
    elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("0" <= patente[2] <= "9") and ("0" <= patente[3] <= "9") and ("0" <= patente[4] <= "9") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
        return 'cbol' #"Boliviana."
    elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("0" <= patente[3] <= "9") and ("A" <= patente[4] <= "Z") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
        return 'cbra'  #"Brasileña."
    elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("A" <= patente[3] <= "Z") and ("0" <= patente[4] <= "9") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
        return 'cpar' #"Paraguaya."
    elif ("A" <= patente[0] <= "Z") and ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("0" <= patente[3] <= "9") and ("0" <= patente[4] <= "9") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
        return 'curu' #"Uruguaya."
    elif ("A" <= patente[1] <= "Z") and ("A" <= patente[2] <= "Z") and ("A" <= patente[3] <= "Z") and ("A" <= patente[4] <= "Z") and ("0" <= patente[5] <= "9") and ("0" <= patente[6] <= "9"):
        return 'cchi' #"Chilena."
    elif len(patente) == 7:
        return 'cotr'  #"Otra (Su patente no corresponde al mercosur, formato desconocido)."

#-----------------------------------------------------------------------------------------------------------------------
 # Programa principal.
#-----------------------------------------------------------------------------------------------------------------------
pruebas = open('peajes.txt', 'rt')
primera_linea = True
segunda_linea = True
kilometros_argentina = 0
paso_por_brasil = 0
imp_acu_total = 0
mayimp = 0
maypat = ''
carg = cbol = cbra = cchi = cpar = curu = cotr = cpp =0
for linea in pruebas:
    if primera_linea:
        idioma = obtener_idioma(linea)
        primera_linea = False
    else:
        patente = linea[0:7]
        tipo_vehiculo = int(linea[7])
        forma_pago = int(linea[8])
        pais_de_cabina = int(linea[9])
        kilometros_recorridos = float(linea[10:13])
        nacionalidad = detector_de_pais(patente)
        importe_final = obtener_importe_final(tipo_vehiculo , pais_de_cabina , forma_pago)
        imp_acu_total += importe_final
        #print('+++++++++++++++++++++++++++++++++++++++++++++')
        #print(linea)
        #print(importe_final)
        #print('nacionalidad::::' , nacionalidad)
        #print('tipo vehiculo:', tipo_vehiculo)
        #print('forma de pago' , forma_pago)
        #print('pais de la cabina:', pais_de_cabina)
        #print('kilometros recorridos:', kilometros_recorridos)
        if segunda_linea:
            primera = linea[0:7]
            segunda_linea = False


        if nacionalidad == 'carg':
            carg += 1
            if pais_de_cabina == 2:
                paso_por_brasil += 1
                kilometros_argentina += int(kilometros_recorridos)
        elif nacionalidad == 'cbol':
            cbol += 1
        elif nacionalidad == 'cbra':
            cbra += 1
        elif nacionalidad == 'cpar':
            cpar += 1
        elif nacionalidad == 'curu':
            curu += 1
        elif nacionalidad == 'cchi':
            cchi += 1
        elif nacionalidad == 'cotr':
            cotr += 1

        if patente == primera:
            cpp += 1

        if importe_final > mayimp:
            mayimp = importe_final
            maypat = patente


prom = calculo_de_kilometros(paso_por_brasil , kilometros_argentina)
porc = calculo_de_porcentaje(carg , cbol , cbra , cchi , cpar , curu , cotr)

#-----------------------------------------------------------------------------------------------------------------------
# Ticket
#-----------------------------------------------------------------------------------------------------------------------
print('(r1) - Idioma a usar en los informes:', idioma)
print()
print('(r2) - Cantidad de patentes de Argentina:', carg)
print('(r2) - Cantidad de patentes de Bolivia:', cbol)
print('(r2) - Cantidad de patentes de Brasil:', cbra)
print('(r2) - Cantidad de patentes de Chile:', cchi)
print('(r2) - Cantidad de patentes de Paraguay:', cpar)
print('(r2) - Cantidad de patentes de Uruguay:', curu)
print('(r2) - Cantidad de patentes de otro país:', cotr)
print()
print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)
print()
print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición:', cpp)
print()
print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:', maypat)
print()
print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
print()
print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')



#print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#print('La nacionalidad del vehiculo es: ',nacionalidad)
#print('su patente es:' , patente)
#print('kilometros argentinos recorridos', kilometros_argentina ,'y paso ' , paso_por_brasil, 'veces por brasil')
#print('la primer patente es:', primera ,'y aparece', cpp, ' veces')