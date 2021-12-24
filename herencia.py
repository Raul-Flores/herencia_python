class Vehiculos():
    def __init__(self, marca:str, modelo:int) -> None:
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self)->bool:
        self.enmarcha=True
    def acelerar(self)->bool:
        self.acelera=True
    def frenar(self)->bool:
        self.frenar=True
    def estado(self)->str:
        print (f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self)->str:
        self.hcaballito="voy haciendo el caballito"
    def estado(self)->str:
        print (f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.hcaballito}")

class Furgoneta(Vehiculos):
    def carga(self,cargar:bool)->str:
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class VElectricos(Vehiculos):
    def __init__(self,marca:str,modelo:int)->None:
        super().__init__(marca,modelo)
        self.autonomia=100
        self.cargando=False
    def cargarEnergia(self)->bool:
        self.cargando=True
    def estado(self)->str:
        super().estado()
        print (f"Autonomia: {self.autonomia}\nCargando: {self.cargando}")

class BicicletaElectrica(VElectricos,Vehiculos):
    pass

#Zona de instancias
print ("#"*40)
miBici = BicicletaElectrica("Tesla Bici",2022)
miBici.cargarEnergia()
miBici.estado()
print ("#"*40)
miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()
print ("#"*40)
miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print (miFurgoneta.carga(True))






