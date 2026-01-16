#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Conceerned with storin and retrieving books from a list
"""

books =[]

def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})

def get_all_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

"""def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)
            
 Esto esta considerado una mala tractica porque la lista queda inconsistente           
 """
def delete_book(name):
    global books #Estamos haciendo referencia a la lista books de inicio que es global, 
                 #esto es por el ambito(scope) de las variables, que dentro de la funcion
                 #serian si no locales
    books = [book for book in books if book['name'] != name]
