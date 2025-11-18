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
       return (f"Título: {self.titulo}\n"
               f"Autor: {self.autor}\n"
               f"Ano: {self.ano}\n"
               f"Número de páginas: {self.numPaginas}\n"
               f"Valoración: {self.valoracion}")






mi_libro = Libro("Harry Pother y el caliz de fuego", "JK Rowling",2008, 455, "9/10")
print (mi_libro.get_titulo())
print (mi_libro.amosarLibro())



