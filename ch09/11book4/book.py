#@@range_begin(list1)
class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.author_data = data['author']  # <1>

    @property
    def author_for_display(self):  # <2>
        return f'{self.author_data["first_name"]} {self.author_data["last_name"]}'

    @property
    def author_for_citation(self):  # <3>
        return f'{self.author_data["last_name"]}, {self.author_data["first_name"][0]}.'
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


print(book.author_for_display) # ウェブ表示用
print(book.author_for_citation) # 論文参考文献用
#@@range_end(list2)
