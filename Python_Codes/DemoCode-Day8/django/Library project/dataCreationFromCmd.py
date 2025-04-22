from library.models import Author, Book, Member

# Add an author
author = Author.objects.create(name="J.K. Rowling", birth_date="1965-07-31")

# Add a member
member = Member.objects.create(name="Alice Smith", email="alice@example.com")

# Add a book
book = Book.objects.create(
    title="Harry Potter and the Philosopher's Stone",
    author=author,
    isbn="9780747532743",
    available=True
)
