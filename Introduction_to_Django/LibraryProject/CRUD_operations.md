````markdown
# CRUD Operations (Django Shell)

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.id
book
# expected:
# - integer id (e.g., 1)
# - <Book: 1984>
```
````
