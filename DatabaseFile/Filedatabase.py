#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:
name,author,read\n
"""

books_file = 'books.txt'

def create_book_table():
    try:
        with open(books_file, 'x') as file:
            pass #No hacemos nada, solo crear el fichero

    except FileExistsError:
        pass #El fichero ya existe, no pasa nada
    except OSError as e:
        print(f"Error al crear el fichero: {e}")
 
def add_book(name, author):
    try:
        with open(books_file, 'a') as file:
            file.write(f'{name},{author},0\n') #Cero for false, one for true

    except OSError as e:
        print(f"Error al escibir en el fichero: {e}")

def get_all_books():
    #[[name, author,read], [name, author,read]]
    try:
        with open(books_file, 'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]

        return [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]
    
    except FileNotFoundError:
        print("El fichero no existe todavía, devolviendo lista vacía.")
        return []
    except Exception as e:
        print(f"Error al leer el fichero: {e}")
        return []

"""books = [
                {'name': line[0], 'author': line[1], 'read': line[2]}
                for line in lines
            ]
    return books
"""

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def delete_book(name):
   books = get_all_books()
   books = [book for book in books if book['name'] != name]
   _save_all_books(books)

        
def _save_all_books(books): #el simbolo _ quiere decir que es una funcion privada por convencion
    try:
        with open(books_file, 'w') as file:
            for book in books:
                file.write(f"{book['name']}, {book['author']} ,{book['read']}\n")
                #file.write(f"{book['name'], book['author'], book['read']}\n")
                
    except OSError as e:
        print(f"Error al guardar los libros: {e}")
        
"""
Ese f"{...}" con varias variables separadas por comas dentro de las llaves no está concatenando cadenas,
 sino que está creando una tupla. Python convierte esa tupla a texto con paréntesis y comillas, 
 y por eso en tu archivo ves cosas como:

('de juan', 'juan', '1')
"""
