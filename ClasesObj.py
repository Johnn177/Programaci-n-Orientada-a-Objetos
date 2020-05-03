class Libro():
    def __init__(self, autor, edicion, titulo):
        self.autor = autor
        self.edicion = edicion
        self.titulo = titulo
    def __str__(self):
        return "Titulo: {}, Autor: {}, Edicion: {}".format(self.titulo, self.autor,self.edicion)
    def pasar_pag(self):
        print("Se paso de pagina")
    def abrir_lib(self):
        print("Se abrio el Libro")
    def cerrar_lib(self):
        print("Se cerro el libro \n")
class Television():
    def __init__(self, color, marca, tamaño, tipo):
        self.color = color
        self.marca = marca
        self.tamaño = tamaño
        self.tipo = tipo
    def __str__(self):
        return "Television Marca: {}, Color: {}, Tamaño {}, Tipo: {}".format(self.marca, self.color,self.tamaño,self.tipo)
    def prender(self):
        print("La Televsion se encendio")
    def apagar(self):
        print("La Televsion se apago")
    def bajar_vol(self):
        print("El volumen se bajo 1Pt")
    def subir_vol(self):
        print("El volumen se subio 1Pt")
Libro1 = Libro("Gabriel Garcia Marquez","2001","Cien años de Soledad")
print(Libro1)
Libro1.abrir_lib()
Libro1.pasar_pag()
Libro1.pasar_pag()
Libro1.pasar_pag()
Libro1.cerrar_lib()

Tv = Television(color="Negro", marca="Samsung", tamaño="15 pulg.", tipo="Curved")
print(Tv)
Tv.prender()
Tv.subir_vol()
Tv.subir_vol()
Tv.subir_vol()
Tv.bajar_vol()
Tv.apagar()
