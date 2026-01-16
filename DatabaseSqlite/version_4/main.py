# SQLModel Tutorial for Beginners
#https://youtu.be/RU6Fk6bmBk8?si=Vjf2KvjPg4fWQL4n
from sqlmodel import SQLModel, create_engine, Session, select, Relationship, Field

engine = create_engine("sqlite:///bibliquitorm.db", echo=True)

class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=50, unique=True)

    books: list["Book"] = Relationship(back_populates="author")

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str
    author_id: int = Field(default=None, foreign_key="author.id")
    
    author: Author = Relationship(back_populates="books")

SQLModel.metadata.create_all(engine)

# Create authors and books
#with Session(engine) as session:
    #author1 = Author(name="Jane Doe", email="jane@example.com")
    #author2 = Author(name="John Smith", email="john@example.com")
    #book1 = Book(title='Alice First Post', content='This is the content of the Alice first post.', author=author1)
    #book2 = Book(title='Bob First Post', content='This is the content of the Bob first post.', author=author1)
    #book3 = Book(title='Alice Second Post', content='This is the content of the Alice second post.', author=author2)

    #session.add_all([author1, author2, book1, book2, book3])
    #session.commit()

# Querys authors and their books
with Session(engine) as session:
    #statement = select(Book)
    #results = session.exec(statement)
    #for book in results:
        #print(book)

    #results = session.exec(statement).all()
    results = session.exec(select(Book)).all()
    print(results)

    statement = select(Book).where(Book.title == "Alice First Post")
    results = session.exec(statement)
    print(results)

    statement = select(Book).where(Book.title.contains("First"))
    results = session.exec(statement)
    for book in results:
        print(f"{book.title} - {book.content}")

    #statement = select(Book, Author).where(Book.author_id == Author.id)
    statement = select(Book, Author).join(Author)
    results = session.exec(statement)
    for book, author in results:
        print(f"{book.title} is written by {author.name}")

    #update book content
    book_to_update = session.exec(select(Book).where(Book.title == "Alice First Post")).first()
    if book_to_update:
        book_to_update.title = "Alice's Updated First Post"
        session.add(book_to_update)
        session.commit()
        session.refresh(book_to_update)
        print(f"Updated Book: {book_to_update}")

    #delete a book
    book_to_delete = session.exec(select(Book).where(Book.title == "Bob First Post")).first()
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()
        print(f"Deleted Book: {book_to_delete}")

    # Verify deletion
    remaining_books = session.exec(select(Book)).all()
    print(f"Remaining Books: {remaining_books}")

                                
    
