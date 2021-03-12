class Empleados:
    def __init__(self, nombre, apellidos, salario):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__salario = salario

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def salario(self):
        return self.__salario

    @staticmethod
    def desde_cadena(str):
        lista = str.split('-')
        return Empleados(lista[0], lista[1], lista[2])


emp1 = Empleados('María', 'García', 60000)
emp2 = Empleados.desde_cadena('Juan-Pérez-55000')
print(emp1.nombre())
print(emp1.salario())
print(emp2.nombre())
print(emp2.salario())
