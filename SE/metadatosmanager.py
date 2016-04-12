class MetaDataManager:
    def __init__(self, archivo, ruta):
        self.archivo = archivo
        self.ruta = ruta
        self.setMetaDatos(self.archivo)

    def crearArchivo(self, nombre, ruta):
        pass

    def setMetaDatos(self, archivo):
        # referencia FILE.csv
        self.metadatos = archivo

    def setMetaDatos(self, MetaDato):
        # referencia FILE.csv
        self.metadatos = MetaDato

    def getMeTadatosFile(self):
        pass
