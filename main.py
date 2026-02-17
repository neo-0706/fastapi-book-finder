from fastapi import FastAPI
from typing import List

books = [
    {
        "id": 1, 
        "title": "The Great Gatsby", 
        "author": "F. Scott Fitzgerald", 
        "publisher": "Scribner"
    },
    {
        "id": 2, 
        "title": "To Kill a Mockingbird", 
        "author": "Harper Lee", 
        "publisher": "J.B. Lippincott & Co."
    },
    {
        "id": 3, 
        "title": "1984", 
        "author": "George Orwell", 
        "publisher": "Secker & Warburg"
    },
    {
        "id": 4, 
        "title": "The Hobbit", 
        "author": "J.R.R. Tolkien", 
        "publisher": "George Allen & Unwin"
    },
    {
        "id": 5, 
        "title": "Animal Farm", 
        "author": "George Orwell", 
        "publisher": "Secker & Warburg"
    },
    {
        "id": 6, 
        "title": "Brave New World", 
        "author": "Aldous Huxley", 
        "publisher": "Chatto & Windus"
    }
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


