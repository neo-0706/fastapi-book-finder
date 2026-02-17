# fastapi-book-finder
# 📚 FastAPI Book Finder

A simple yet powerful Search API that mimics a real-world bookstore backend.

## 🚀 Key Features
- **Smart Filtering:** Search through titles, authors, and publishers simultaneously.
- **Query Params:** Utilizes FastAPI's query system for dynamic data retrieval.
- **In-Memory DB:** Efficiently handles a collection of book records using Python dictionaries.
- **Interactive UI:** A minimal frontend to test the search functionality in real-time.

## 🛠️ How it works
The backend takes a search query `q` and performs a case-insensitive search across multiple fields:
```python
# The Logic
if q.lower() in book["title"].lower() or q.lower() in book["author"].lower() ...
