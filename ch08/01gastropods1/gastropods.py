class Slug:  # ナメクジ
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print(f'{self.name}の這い跡ができました')


class Snail(Slug):  # <1>  # カタツムリ   Slug（ナメクジ）を継承
    def __init__(self, name, shell_size):  # <2>
        super().__init__(name)
        self.name = name
        self.shell_size = shell_size   # 殻の大きさ


def race(gastropod_one, gastropod_two):
    gastropod_one.crawl()
    gastropod_two.crawl()


race(Slug('小次郎'), Slug('小雪'))  # <3>
race(Snail('小次郎'), Snail('小雪'))  # <4>
