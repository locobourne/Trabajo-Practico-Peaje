#-----------------------------------------------------------------------------------------------------------------------
 # Funciones a utilizar.
#-----------------------------------------------------------------------------------------------------------------------

def obtener_idioma(linea):
    anterior = ''
    cont_letras = pal_3let = cant_pal = pal_terminan_s = pal_dre = 0
    tiene_d = tiene_dr = tiene_dre = False
    for letra in texto:
        if letra == ' ' or letra == '.':
            if cont_letras > 0:
                cant_pal += 1

                if cont_letras == 3:
                    pal_3let += 1

                if anterior == 's':
                    pal_terminan_s += 1

                if tiene_dre:
                    pal_dre += 1

                tiene_dre = False
                cont_letras = 0
        else:
            cont_letras += 1
            if letra == 'd':
                tiene_d = True
                tiene_dr = False
            else:
                if letra == 'r' and tiene_d:
                    tiene_dr = True
                else:
                    if letra == 'e' and tiene_dr:
                        tiene_dre = True
                    tiene_dr = False
                tiene_d = False
            anterior = letra








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
