import json
import random

class Procesamiento:

    def __init__(self):
        self.nombres = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Edison", "Gertrudis", "Rafaella", "Tulio", "Laura", "Carlos", "Miguel", "Elena", "Sofia"]
        self.data = None
        self.lista_mensajes = []
        self.mejores_amigos = []
        self.menos_amigos = []
        self.mensajes_enviados = []
        self.mensajes_recibidos = []

    def generar_relacion(self, id_emisor, id_receptor):
        mensaje = f"Hola {self.nombres[id_receptor]}, soy {self.nombres[id_emisor]}. Amigos!!!."
        relacion = {
            "id_emisor": id_emisor,
            "nombre_emisor": self.nombres[id_emisor],
            "id_receptor": id_receptor,
            "nombre_receptor": self.nombres[id_receptor],
            "mensaje": mensaje
        }
        return relacion

    def generar_relaciones(self, cantidad):
        # Número de relaciones que deseas generar
        n = cantidad

        # Lista para almacenar las relaciones
        relaciones = []

        # Generar n relaciones y agregarlas a la lista
        for _ in range(n):
            id_emisor = random.randint(0, 13)
            id_receptor = random.randint(0, 13)
            while (id_emisor == id_receptor):
                id_receptor = random.randint(0, 13)
            relacion = self.generar_relacion(id_emisor, id_receptor)
            relaciones.append(relacion)

        # Guardar la lista de relaciones en un archivo JSON
        with open('C:/Users/aleja/PycharmProjects/proyecto_final_datos/historial_comunicaciones.json',
                  "w") as archivo_json:
            json.dump(relaciones, archivo_json, indent=2)

        print(f"Se han generado y guardado {n} relaciones en el archivo 'historial_comunicaciones.json'.")

        with open('C:/Users/aleja/PycharmProjects/proyecto_final_datos/historial_comunicaciones.json') as file:
            self.data = json.load(file)

    def obtener_resultados(self):
        try:
            for i in self.nombres:
                cont = 0
                for j in self.nombres:
                    if i == j:
                        continue
                    for x in self.data:
                        if x["nombre_emisor"] == i and x["nombre_receptor"] == j:
                            cont += 1
                        if x["nombre_emisor"] == j and x["nombre_receptor"] == i:
                            cont += 1
                    self.lista_mensajes.append([i, j, cont])

            for x in self.nombres:
                for j in self.lista_mensajes:
                    if j[0] == x:
                        menor = j
                        mayor = j
                        break
                for i in self.lista_mensajes:
                    if x == i[0]:
                        if menor[2] > i[2]:
                            menor = i
                        if mayor[2] < i[2]:
                            mayor = i
                self.mejores_amigos.append(mayor)
                self.menos_amigos.append(menor)

            print("-" * 100)
            print("                             MEJORES AMIGOS               ")
            print("-" * 100)
            for i in self.mejores_amigos:
                print(f"El mejor amigo de {i[0]} es {i[1]} con {i[2]} mensajes intercambiados.")
                print("-" * 100)
            print("                             PEORES AMIGOS               ")
            print("-" * 100)
            for i in self.menos_amigos:
                print(f"El peor amigo de {i[0]} es {i[1]} con {i[2]} mensajes intercambiados.")
                print("-" * 100)

        except Exception as error:
            print(f"Error: {error}")
            return f"Error: {error}"

    def mensajes(self):
        try:
            # determinar quien envio y recibio mas y menos mensajes
            menor = 0
            mayor = 0
            for i in self.nombres:
                cont = 0
                for j in self.nombres:
                    if i == j:
                        continue
                    for x in self.data:
                        if x["nombre_emisor"] == i and x["nombre_receptor"] == j:
                            cont += 1
                    self.mensajes_enviados.append([i, j, cont])

            for i in range(len(self.mensajes_enviados)):
                for j in range(i + 1, len(self.mensajes_enviados)):
                    if self.mensajes_enviados[j][2] < self.mensajes_enviados[i][2]:
                        menor = j
                    if self.mensajes_enviados[j][2] > self.mensajes_enviados[mayor][2]:
                        mayor = j

            # imprimir persona que envio y recibio mas y menos mensajes
            print(f"La persona que envio menos mensajes es {self.mensajes_enviados[menor][0]} con {self.mensajes_enviados[menor][2]} mensajes")
            print(f"La persona que envio más mensajes es {self.mensajes_enviados[mayor][0]} con {self.mensajes_enviados[mayor][2]} mensajes")

            # determianr quien recibio menos y mas mensajes
            for i in self.nombres:
                cont = 0
                for j in self.nombres:
                    if i == j:
                        continue
                    for x in self.data:
                        if x["nombre_receptor"] == i and x["nombre_emisor"] == j:
                            cont += 1
                    self.mensajes_recibidos.append([i, j, cont])

            menor = 0
            mayor = 0
            for i in range(len(self.mensajes_recibidos)):
                for j in range(i + 1, len(self.mensajes_recibidos)):
                    if self.mensajes_recibidos[j][2] < self.mensajes_recibidos[i][2]:
                        menor = j
                    if self.mensajes_recibidos[j][2] > self.mensajes_recibidos[mayor][2]:
                        mayor = j

            # imprimir persona que envio y recibio mas y menos mensajes
            print(f"La persona que recibio menos mensajes es {self.mensajes_recibidos[menor][1]} con {self.mensajes_recibidos[menor][2]} mensajes")
            print(f"La persona que recibio más mensajes es {self.mensajes_recibidos[mayor][1]} con {self.mensajes_recibidos[mayor][2]} mensajes")

        except Exception as error:
            print(f"Error: {error}")
            return f"Error: {error}"

    def menu(self):
        p = Procesamiento()
        print("\nBienvenidos al Whatsapp de Eafit\n")
        while True:
            opc = int(input("\nIngrese una de las opciones:\n1.Ingresar cuantos mensajes/datos quiere\n2.Obtener los lazos de amistad más fuertes y menos fuertes\n3.Obtener quién recibio y quién envio más y menos mensajes\n4.Acabar programa\n->"))
            if opc == 1:
                p.generar_relaciones(int(input("Cuantos datos desea generar?: ")))
            elif opc == 2:
                p.obtener_resultados()
            elif opc == 3:
                p.mensajes()
            elif opc == 4:
                print("Bye!!!!")
                exit()