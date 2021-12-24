class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    def descripcion(self):
        print (f"Nombre: {self.nombre}\nEdad: {self.edad}\nResidencia: {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self,salario,antiguiedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguiedad
    def descripcion(self):
        super().descripcion()
        print (f"Salario: {self.salario}\nAntiguedad: {self.antiguedad}")

Antonio=Persona("Antonio",33,"Guatemala")
Antonio.descripcion()

Raul=Empleado(1500,15,"Raul",33,"Guatemala")
Raul.descripcion()



print (isinstance(Antonio,Empleado))