class Book:
    def __init__(self, id, title, author, publishers, year, page_q, price, cover, book_list = []):
        self.title = title
        self.id = id
        self.author = author
        self.publishers = publishers
        self.year = year
        self.page_q = page_q
        self.price = price
        self.cover = cover
        self.book_list = book_list

    def add_book(self, books):
        self.book_list.append(books)

    def get_author_book(self):
        choice = str(input('choose author '))
        author_list = []
        for book in self.book_list:
            if book[2] == choice:
                author_list.append(book[1])
        return author_list

    def get_publisher_books(self):
        choice = str(input('choose publishing house '))
        publ_list = []
        for book in self.book_list :
            if book[3] == choice :
                publ_list.append(book[1])
        return publ_list

    def get_year_after_books(self):
        choice = int(input('choose year '))
        year_list = []
        for book in self.book_list :
            if book[4] > choice :
                year_list.append(book[1])
                year_list.append(book[4])
        return year_list

    def save_books(self):
        with open("books.txt", "w") as file_write:
            file_write.write(str(self.book_list))

    def __str__(self):
        return f"{self.id}, {self.title}, {self.author},{self.publishers}, {self.year},\
        {self.page_q},{self.price}, {self.cover}, {self.book_list}"

books_list = Book(56, 'Pride and Prejudice', 'Jane Austin', 'Egerton', 1813, 350, 50, 'hardcover')
book1 = 56, 'Pride and Prejudice', 'Jane Austin', 'Egerton', 1813, 350, 50, 'hardcover'
book2 = 76, 'Harry Potter and Deathly Hallows', 'J.K. Rowling', 'Bloomsberg', 2007, 750, 90, 'hardcover'
book3 = 99, 'Emma', 'Jane Austin', 'Egerton', 1819, 307, 50, 'paperback'
book4 = 33, 'Casual Vacancy', 'J.K. Rowling', 'Bloomsberg', 2013, 530, 80, 'paperback'
book5 = 100, 'Bard Beadle tales', 'J.K. Rowling', 'Bloomsberg', 2010, 207, 100, 'hardcover'
book6 = 30, 'Buddenbrocks', 'Tomas Mann', 'Egerton', 1901, 809,95, 'hardcover'
book7 = 10, 'Uncle Tom Cabin', 'Harriet Beecher Stowe', 'Egerton', 1852, 390, 70, 'paperback'

books = [book1, book2, book3, book4, book5, book6, book7]
for book in books:
    books_list.add_book(book)
print(books_list)
print(books_list.get_author_book())
print(books_list.get_publisher_books())
print(books_list.get_year_after_books())
books_list.save_books()