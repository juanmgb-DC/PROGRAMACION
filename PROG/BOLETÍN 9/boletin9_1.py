class Libro:
    def __init__(self,titulo,autor,ano,numPaginas,valoracion):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.numPaginas = numPaginas
        self.valoracion = valoracion

    def get_titulo (self):
        return self.titulo
    def get_autor (self):
        return self.autor
    def get_ano (self):
        return self.ano
    def get_numPaginas (self):
        return self.numPaginas
    def get_valoracion (self):
        return self.valoracion
    def amosarLibro(self):
        return self.titulo, self.autor, self.ano, self.numPaginas, self.valoracion



mi_libro = Libro('Titulo: Harry Pother y el caliz de fuego', 'Autor: JK Rowling','Ano: 2008', 'Número de páginas: 455', 'Valoración: 9/10')
print (mi_libro.get_titulo())
print (mi_libro.amosarLibro())



