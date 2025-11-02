````markdown
# Update the Book title

```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(id=b.id).title
# expected output:
# 'Nineteen Eighty-Four'
```
````
