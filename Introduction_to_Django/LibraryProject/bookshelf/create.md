# Create a Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.id
book
# expected output:
# - book.id returns an integer primary key (e.g., 1)
# - book prints as <Book: 1984> because __str__ returns the title
```
