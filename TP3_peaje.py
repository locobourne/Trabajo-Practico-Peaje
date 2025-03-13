#-----------------------------------------------------------------------------------------------------------------------
 # Cabina de peaje 3.0
 # Castillo Maximo - 403257 - 1K10
#-----------------------------------------------------------------------------------------------------------------------
import os.path
import pickle
from TP3_funcion_constructora import *


def patente_argentina(patente):
    if len(patente) == 7:
        if (patente[0].isalpha() and
                patente[1].isalpha() and
                patente[2].isdigit() and
                patente[3].isdigit() and
                patente[4].isdigit() and
                patente[5].isalpha() and
                patente[6].isalpha()):
            return True


def patente_brasil(patente):
    if len(patente) == 7:
        if (patente[0].isalpha() and
                patente[1].isalpha() and
                patente[2].isalpha() and
                patente[3].isdigit() and
                patente[4].isalpha() and
                patente[5].isdigit() and
                patente[6].isdigit()):
            return True


def patente_uruguay(patente):
    if len(patente) == 7:
        if (patente[0].isalpha() and
                patente[1].isalpha() and
                patente[2].isalpha() and
                patente[3].isdigit() and
                patente[4].isdigit() and
                patente[5].isdigit() and
                patente[6].isdigit()):
            return True


def patente_bolivia(patente):
    if len(patente) == 7:
        if (patente[0].isalpha() and
                patente[1].isalpha() and
                patente[2].isdigit() and
                patente[3].isdigit() and
                patente[4].isdigit() and
                patente[5].isdigit() and
                patente[6].isdigit()):
            return True


def patente_paraguay(patente):
    if len(patente) == 7:
        if (patente[0].isalpha() and
                patente[1].isalpha() and
                patente[2].isalpha() and
                patente[3].isalpha() and
                patente[4].isdigit() and
                patente[5].isdigit() and
                patente[6].isdigit()):
            return True


def patente_chile(patente):
    if len(patente) == 6:
        if (patente[0].isalpha() and
                patente[1].isalpha() and
                patente[2].isalpha() and
                patente[3].isalpha() and
                patente[4].isdigit() and
                patente[5].isdigit()):
            return True


def identificar_pais(patente):
    if patente_argentina(patente):
        return 0
    elif patente_chile(patente):
        return 5
    elif patente_bolivia(patente):
        return 1
    elif patente_brasil(patente):
        return 2
    elif patente_paraguay(patente):
        return 3
    elif patente_uruguay(patente):
        return 4
    else:
        return 6


def menu():
    print('1. Crear archivo binario')
    print('2. Cargar datos de Ticket')
    print('3. Mostrar datos de los Registros')
    print('4. Mostrar registros de una Patente')
    print('5. Mostrar registros de un Ticket')
    print('6.')
    print('7.')
    print('8.')
    print('9. Salir')


# Carga el archivo binario con registros armados desde el archivo de texto.
def punto_1(tf, bf):
    if os.path.exists(tf):
        print("Creando el archivo de registros...")
        mt = open(tf, "rt")

        # lee e ignora la linea de timestamp...
        ln = mt.readline()

        # lee e ignora la linea de descriptores de columnas...
        ln = mt.readline()

        mb = open(bf, "wb")
        while True:
            ln = mt.readline()

            # control de eof...
            if ln == "":
                break

            tokens = ln.split(",")
            cod = int(tokens[0])
            pat = tokens[1]
            pais = identificar_pais(pat)
            tiv = int(tokens[2])
            fop = int(tokens[3])
            pic = int(tokens[4])
            dis = int(tokens[5])
            tik = Ticket(cod, pat, pais, tiv, fop, pic, dis)
            pickle.dump(tik, mb)

        mt.close()
        mb.close()
        print("Listo...")
    else:
        print("El archivo", tf, "no existe...")
    print()


def validar_tipo():
    x = int(input('Ingrese el tipo de vehiculo 0: motocicleta, 1: automóvil, 2: camión: '))
    while x < 0 or x > 2:
        x = int(input('Error, ingrese 0: motocicleta, 1: automóvil, 2: camión: '))
    return x


def validar_pago():
    x = int(input('Ingrese el tipo de pago 1: manual, 2 telepeaje: '))
    while x < 1 or x > 2:
        x= int(input('Error, ingrese 1: manual - 2 telepeaje: '))
    return x


def validar_cabina():
    x = int(input('Ingrese una cabina, 0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay: '))
    while x < 0 or x > 4:
        x = int(input('Error, ingrese una cabina del 0 al 4: '))
    return x

def validar_distancia():
    x = int(input('Ingrese la distancia recorrida: '))
    while x < 0:
        x = int(input('Error, ingrese una distancia mayor o igual a cero: '))
    return x


def punto_2(bf):
    archivo = open(bf, "ab+")
    t = input('Ingrese el ticket: ')
    p = input('Ingrese la patente: ')
    pais = identificar_pais(p)
    tipo = validar_tipo()
    pago = validar_pago()
    cab = validar_cabina()
    dis = validar_distancia()

    ticket = Ticket(t, p, pais, tipo, pago, cab, dis)

    archivo.seek(0, 2)  # Mover el puntero al final del archivo
    pickle.dump(ticket, archivo)  # Escribir el objeto en el archivo binario
    archivo.close()  # Cerrar el archivo


# Muestra el archivo binario (FALTA mostrar el nombre del país origen de cada patente...)
def punto_3(bf):
    if os.path.exists(bf):
        mb = open(bf, "rb")
        t = os.path.getsize(bf)
        print("Listado de tickets...")
        while mb.tell() < t:
            r = pickle.load(mb)
            print(r)
        mb.close()
        print("Listo...")
    else:
        print("El archivo", bf, "no existe...")
    print()


def crear_matriz(bf):
    if not os.path.exists(bf):
        print("El archivo", bf, "no existe")
        return

    m = open(bf, "rb")
    mc = [[0] * 5 for f in range(3)]
    t = os.path.getsize(bf)
    while m.tell() < t:
        r = pickle.load(m)
        f = r.tipo
        c = r.pais_cabina
        mc[f][c] += 1
    m.close()
    return mc


def punto_6(bf):
    mc = crear_matriz(bf)
    print("Resultados...")
    for f in range(3):
        for c in range(5):
            if mc[f][c] != 0:
                print("Tipo", f, " - País:", c, " - Cantidad:", mc[f][c])
    print()


def punto_7(bf):
    mc = crear_matriz(bf)

    print("Totales por tipo de vehículo")
    for f in range(len(mc)):
        ac = 0.
        for c in range(len(mc[f])):
            ac += mc[f][c]
        print("Tipo:", f, " - Cantidad:", ac)
    print()

    print("Totales por países de cabinas")
    for c in range(len(mc[f])):
        ac = 0
        for f in range(len(mc)):
            ac += mc[f][c]
        print("País:", c, " - Cantidad:", ac)
    print()


# Un main de prueba... Lo demás, les toca a ustedes...
def punto_4(bf, p):
    t = os.path.getsize(bf)
    mb = open(bf, "rb")
    print("Listado de tickets...")
    vuelta = 0
    while mb.tell() < t:
        ticket = pickle.load(mb)
        if ticket.patente == p:
            vuelta += 1
            print(ticket)
    mb.close()
    print('La cantidad de registros que se mostraron fueron:', vuelta)


def punto_5(bf, c):
    t = os.path.getsize(bf)
    mb = open(bf, "rb")
    print("Listado de tickets...")
    hay = False
    while mb.tell() < t:
        ticket = pickle.load(mb)
        if ticket.codigo == c:
            print(ticket)
            hay = True
            break
    if hay is False:
        print('No se encontro dicho codigo')
    mb.close()

def promedio(bf):
    t = os.path.getsize(bf)
    mb = open(bf, "rb")
    print("Calculando promedio...")
    vuelta = 0
    suma = 0
    while mb.tell() < t:
        ticket = pickle.load(mb)
        suma += ticket.km_recorridos
        vuelta += 1
    promedio_km = suma / vuelta
    return round(promedio_km, 2)

def mostrar_vec(vec):
    for i in vec:
        print(i)

def shellsort(vec):
    n = len(vec)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1

    while h > 0:
        for j in range(h, n):
            y = vec[j]
            k = j - h
            while k >= 0 and y.km_recorridos < vec[k].km_recorridos:
                vec[k + h] = vec[k]
                k -= h
            vec[k + h] = y
        h //= 3

def punto_8(bf, promedio_km, vec):
    t = os.path.getsize(bf)
    mb = open(bf, "rb")
    print("Comparando promedios...")
    while mb.tell() < t:
        ticket = pickle.load(mb)
        if ticket.km_recorridos >= promedio_km:
            vec.append(ticket)
    mb.close()



def main():
    tf = "peajes-tp3.csv"
    bf = "tickets-pt3.dat"
    op = 0
    vec = []
    while op != 9:
        menu()
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            punto_1(tf, bf)
        elif op == 2:
            punto_2(bf)
        elif op == 3:
            punto_3(bf)
        elif op == 4:
            p = input('Ingrese patente a buscar: ')
            print()
            punto_4(bf, p)
        elif op == 5:
            c = int(input('Ingrese codigo a buscar: '))
            punto_5(bf, c)
        elif op == 6:
            punto_6(bf)
        elif op == 7:
            punto_7(bf)
        elif op == 8:
            promedio_km = promedio(bf)
            punto_8(bf, promedio_km,vec)
            shellsort(vec)
            mostrar_vec(vec)
            print('El promedio de kilometros recorridos es de: ', promedio_km, 'km')

        elif op == 9:
            print('Gracias por usar el programa...')


if __name__ == "__main__":
    main()
