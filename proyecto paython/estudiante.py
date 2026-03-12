class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Notas:", self.notas)



est1 = Estudiante("Juan", 20)


est1.agregar_nota(90)
est1.agregar_nota(80)
est1.agregar_nota(85)


est1.mostrar_info()


print("Promedio:", est1.calcular_promedio())