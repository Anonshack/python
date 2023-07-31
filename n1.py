class Book:
      def __init__ (self, id, title, content):
            self.id = id
            self.title = title
            self.content = content
            self.last_page = 0

      def display_page (self):
            return self.content[self.last_page]

      def turn_page (self):
            self.last_page += 1
            return self.display_page

      def __repr__ (self):
            info = f"ID: {self.id} Title: {self.title} Content: {self.content}"
            return info


book1 = Book(12, "Umar_Hattob", "Beautiful");
print(book1);


class Libraly:
      def __init__ (self):
            self.collection = dict()
            self.active_book = None
            self.if_counter = 0

      def add_to_collection (self, title, content):
            new_book = Book(self.id_counter, title, content)
            self.collection[new_book.id] = new_book
            self.if_counter += 1

      def remove_from_collection (self, id):
            del self.collection[id]

      def set_active_book (self, id):
            self.active_book = id

      def display_page (self):
            return self.collection[self.active_book].display_page();

      def turn_page (self):
            return self.collection[self.active_book].turn_page();

