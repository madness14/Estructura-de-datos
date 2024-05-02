# Crea una clase llamada Libro que tenga
# atributos como título, autor, género,
# y año de publicación. Luego, crea una
# clase Biblioteca que contenga una lista
# de libros. Implementa métodos para
# agregar un libro nuevo, buscar un libro
# por título y eliminar un libro de la
# biblioteca.

class Libro:
    def __init__(self, titulo, autor, genero, year):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.year = year
    
    def mostrar_libro(self):
        print('Titulo:', self.titulo)
        print('Autor:', self.autor)
        print('Genero:', self.genero)
        print('Anio de publicacion:', self.year, '\n')

class Biblioteca(Libro):
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def buscar_libro(self, titulo):
        for i in self.libros:
            if i.titulo == titulo:
                return i
            
    def eliminar_libro(self, titulo):
        for i in self.libros:
            if i.titulo == titulo:
                self.libros.remove(i)        
    
libro1 = Libro('Libro troll', 'Rubiusomg', 'Comedia', 2049)
libro2 = Libro('La llamada de Cthulhu', 'H.P. Lovecraft', 'Horror', 1820)
libro3 = Libro('Libro Vaquero', 'Un random', 'Erotismo', 1900)

biblioteca = Biblioteca()


biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

titulo_buscado = input()
libro_encontrado = biblioteca.buscar_libro(titulo_buscado)
if libro_encontrado:
    print('Libro encontrado:', titulo_buscado)
else:
    print('No encontrado: ', titulo_buscado)

titulo_a_eliminar = input()
biblioteca.eliminar_libro(titulo_a_eliminar)
print('\nTitulo eliminado: ', titulo_a_eliminar)

print('\nLibros restantes: ')
for i in biblioteca.libros:
    i.mostrar_libro(),
