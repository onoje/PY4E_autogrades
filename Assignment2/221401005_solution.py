############ Do not change the assignment code value ############
assignment_code = 140110202
name = "Elif"
surname = "Duran"
student_id = "221401005"
### Do not change the variable names above, just fill them in ###

import json


class Book:
    def __init__(self, title, author, publish_date, isbn, is_borrow=False, borrower=None):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.isbn = isbn
        self.is_borrowed = is_borrow
        self.borrower = borrower


class User:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.data_file = "library_data.json"
        self._load_data()

    def _save_data(self):
        books_data = []
        for book in self.books:
            book_data = {
                'title': book.title,
                'author': book.author,
                'publish_date': book.publish_date,
                'isbn': book.isbn,
                'is_borrowed': book.is_borrowed,
                'borrower': book.borrower,
            }
            books_data.append(book_data)

        users_data = []
        for user in self.users:
            user_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'student_id': user.student_id
            }
            users_data.append(user_data)

        with open(self.data_file, 'w', encoding="utf-8") as file:
            json.dump({
                'books': books_data,
                'users': users_data,
            }, file, indent=2, ensure_ascii=False)

    def _load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for book_data in data.get('books', []):
                    title = book_data['title']
                    author = book_data['author']
                    publish_date = book_data['publish_date']
                    isbn = book_data['isbn']
                    is_borrowed = book_data.get('is_borrowed', False)
                    borrower = book_data.get('borrower', None)

                    book_obj = Book(title, author, publish_date, isbn, is_borrowed, borrower)
                    self.books.append(book_obj)

                for user_data in data.get('users', []):
                    first_name = user_data['first_name']
                    last_name = user_data['last_name']
                    student_id = user_data['student_id']
                    user_obj = User(first_name, last_name, student_id)
                    self.users.append(user_obj)

        except FileNotFoundError:
            self._save_data()

    def add_book(self, title, author, publish_date, isbn):
        for a in self.books:
            if a.isbn == isbn:
                return False

        a = Book(title, author, publish_date, isbn)
        self.books.append(a)
        self._save_data()
        return True

    def add_user(self, first_name, last_name, student_id):
        for b in self.users:
            if b.student_id == student_id:
                return False

        b = User(first_name, last_name, student_id)
        self.users.append(b)
        self._save_data()
        return True

    def check_book_by_isbn(self, isbn):
        for c in self.books:
            if c.isbn == isbn:
                return True
        return False

    def remove_book(self, isbn):
        for d in self.books:
            if d.isbn == isbn:
                self.books.remove(d)
                self._save_data()
                return d.title
        return False

    def delete_user(self, student_id):
        for e in self.users:
            if e.student_id == student_id:
                for f in self.books:
                    if f.borrower == e.student_id:
                        return False

            self.users.remove(e)
            self._save_data()
            return e.student_id

    def list_books(self):
        g = list()
        for h in self.books:
            g.append(h.isbn)
        return g

    def borrow_book(self, isbn, student_id):
        for i in self.users:
            if i.student_id == student_id:
                for j in self.books:
                    if j.isbn == isbn:
                        j.is_borrowed = True
                        j.borrower = i.student_id
                        self._save_data()
                        return True
                    else:
                        return False
            else:
                return False

    def return_book(self, isbn):
        for k in self.books:
            if k.isbn == isbn and k.is_borrowed == True:
                k.is_borrowed = False
                k.borrower = None
                self._save_data()
                return True

        return False


"""
library = Library()
print(library.add_book('The Call of the Wild', 'Jack London', '1903', 9781945644511))
print(library.add_book('Animal Farm', 'George Orwell', '2003', 9780452284241))
print(library.add_user('Selim', 'Altay', 15040203))
print(library.add_user('Aylin', 'Kaya', 17140107))
print(library.check_book_by_isbn(9780452284241))
print(library.remove_book(9781945644511))
print(library.delete_user(15040203))
print(library.list_books())
print(library.borrow_book(9780452284241, 17140107))
print(library.return_book(9780452284241))
"""
