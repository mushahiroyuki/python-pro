#@@range_begin(list1)
class Book:
    def __init__(self, title, subtitle, author):
        self.title = title
        self.subtitle = subtitle
        self.author = author

    def display_info(self):  # <1>
        print(f'{self.author}著『{self.title} ── {self.subtitle}』')  # <2>        
#@@range_end(list1)


book = Book(author='デイン・ディラード', title='Pythonプロフェッショナル・プログラミング', subtitle='一流のPythonプログラマーへのパスポート')
book.display_info()

