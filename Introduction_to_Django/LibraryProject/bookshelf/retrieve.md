````markdown
# Retrieve the created Book

```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.id, b.title, b.author, b.publication_year
# expected output:
# (1, '1984', 'George Orwell', 1949)
```
````
