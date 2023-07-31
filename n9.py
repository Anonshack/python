class Book:
    def __init__(self, book_type: str, book_name: str, author: str, title: str, years: int):
        self.book_type = book_type
        self.book_name = book_name
        self.author = author
        self.title = title
        self.years = years

    def about_book(self):
        info = f"Name: {self.book_name}, Type: {self.book_type}, Muallifi: {self.author}, Title: {self.title}, Yili: {self.years}."
        return info

    def change_title(self, new_title):
        self.title = new_title

    def change_author(self, new_author):
        self.author = new_author

    def get_details(self):
        about = f"Name: {self.book_name}, Type: {self.book_type}, Muallifi: {self.author}, Title: {self.title}, Yili: {self.years}."
        return about

book1 = Book("Interesting", "Python", "Umar", "Beautiful", 2019);
book2 = Book("Light", "C++", "Saud", "Strong", 2020);

# book1.change_title('Beautiful') #shu yordamida o'zgartiriladi
# book1.change_author('Qudratbek')
print(book1.get_details())
print(book2.get_details())
