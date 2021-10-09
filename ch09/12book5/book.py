#@@range_begin(list1)
class Author:
    def __init__(self, author_data):  # <1>
        self.first_name = author_data['first_name']
        self.last_name = author_data['last_name']

    @property
    def for_display(self):  # <2>
        return f'{self.first_name} {self.last_name}'

    @property
    def for_citation(self):
        return f'{self.last_name}, {self.first_name[0]}.'


class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.author_data = data['author']  # <3>
        self.author = Author(self.author_data)  # <4>

    @property
    def author_for_display(self):  # <5>
        return self.author.for_display

    @property
    def author_for_citation(self):
        return self.author.for_citation
#@@range_end(list1)


#@@range_begin(list2)
book = Book({
    'title': 'Brillo-iant',
    'subtitle': 'The pad that changed everything',
    'author': {
        'first_name': 'Rusty',
        'last_name': 'Potts',
    }
})


print(book.author_for_display)
print(book.author_for_citation)
#@@range_end(list2)
