class Book:
    def __init__(self, data):
        self.title = data['title']  # <1>
        self.subtitle = data['subtitle']

        # 表示用タイトル（display_title）の決定
        if self.title and self.subtitle:  # <2>
            # サブタイトルが指定されているときは、メインのタイトルの後ろに付加する
            self.display_title = f'{self.title}: {self.subtitle}'
        elif self.title:
            # タイトルのみが指定されているときはそれを表示用タイトルにする
            self.display_title = self.title
        else:
            # どちらも指定されていない場合はUntitled（無題）とする
            self.display_title = 'Untitled'
