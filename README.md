# fastapi-book-finder

# 📚 FastAPI Book Search API

A lightweight and efficient Book Search API built with **FastAPI**. This project demonstrates the core principles of backend development, focusing on API routing, query parameter handling, and in-memory data filtering.

## 🚀 Key Features
- **Smart Multi-Field Search:** Search simultaneously across book titles, authors, and publishers.
- **Case-Insensitive Matching:** Optimized search logic that ignores letter casing for better user experience.
- **Dynamic Query Parameters:** Leverages FastAPI's `q` parameter to filter data on the fly.
- **Interactive Documentation:** Built-in support for Swagger UI to test endpoints instantly.

---

## 🛠️ API Architecture

### 1. Root Endpoint
- **Endpoint:** `/`
- **Description:** Returns a welcome message and basic instructions on how to use the API.

### 2. Search Functionality
- **Endpoint:** `/search`
- **Parameter:** `q` (Optional string)
- **Behavior:** - If `q` is empty: Returns the full list of books.
    - If `q` is provided: Returns all books where the query matches the Title, Author, or Publisher.

**Example Request:**
`GET /search?q=orwell`

---

## 💻 Technical Logic
The search engine is powered by a clean Pythonic loop that ensures data accessibility and accuracy:

```python
for book in books:
    # Normalize both query and data to lowercase for a seamless search
    if (q.lower() in book["title"].lower() or 
        q.lower() in book["author"].lower() or 
        q.lower() in book["publisher"].lower()):
        results.append(book)
