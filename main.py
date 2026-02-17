from fastapi import FastAPI
from typing import List

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publisher": "Scribner"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publisher": "J.B. Lippincott & Co."},
    {"id": 3, "title": "1984", "author": "George Orwell", "publisher": "Secker & Warburg"},
    {"id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien", "publisher": "George Allen & Unwin"},
    {"id": 5, "title": "Animal Farm", "author": "George Orwell", "publisher": "Secker & Warburg"},
    {"id": 6, "title": "Brave New World", "author": "Aldous Huxley", "publisher": "Chatto & Windus"},
    {"id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "publisher": "Little, Brown and Company"},
    {"id": 8, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "publisher": "George Allen & Unwin"},
    {"id": 9, "title": "The Alchemist", "author": "Paulo Coelho", "publisher": "HarperCollins"},
    {"id": 10, "title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "publisher": "Reynal & Hitchcock"},
    {"id": 11, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "publisher": "Bloomsbury"},
    {"id": 12, "title": "The Da Vinci Code", "author": "Dan Brown", "publisher": "Doubleday"},
    {"id": 13, "title": "Pride and Prejudice", "author": "Jane Austen", "publisher": "T. Egerton"},
    {"id": 14, "title": "The Old Man and the Sea", "author": "Ernest Hemingway", "publisher": "Scribner"},
    {"id": 15, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "publisher": "The Russian Messenger"},
    {"id": 16, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "publisher": "The Russian Messenger"},
    {"id": 17, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "publisher": "Harper & Row"},
    {"id": 18, "title": "The Shining", "author": "Stephen King", "publisher": "Doubleday"},
    {"id": 19, "title": "The Catch-22", "author": "Joseph Heller", "publisher": "Simon & Schuster"},
    {"id": 20, "title": "Fahrenheit 451", "author": "Ray Bradbury", "publisher": "Ballantine Books"}
]

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Welcome to the Book Search API! Use /search?q=... to find books."}

@app.get('/search')
async def search(q : str = None):
    results: List = []
    if q == None:
        results = books
    else:
        for book in books:
            if q.lower() in  book["title"].lower()  or  q.lower() in  book["publisher"].lower()  or  q.lower() in  book["author"].lower() :
                results.append(book)
                
    return results  


