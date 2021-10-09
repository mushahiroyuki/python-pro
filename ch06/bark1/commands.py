# ch06/bark1/commands.py
import sys
from datetime import datetime

from database import DatabaseManager

#@@range_begin(list1)
db = DatabaseManager('bookmarks.db')  # <1>


class CreateBookmarksTableCommand:
    def execute(self):  # <2>
        db.create_table('bookmarks', {  # <3>
            'id': 'integer primary key autoincrement',
            'タイトル': 'text not null',
            'url': 'text not null',
            'メモ': 'text',
            '追加日時': 'text not null',
        })
#@@range_end(list1)

#@@range_begin(list2)
class AddBookmarkCommand:
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()  # <1>
        db.add('bookmarks', data)  # <2>
        return 'ブックマークを追加しました。'  # <3>
#@@range_end(list2)

#@@range_begin(list3)
class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):  # <1>
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()  # <2>
#@@range_end(list3)

#@@range_begin(list4)
class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})  # <1>
        return 'ブックマークを削除しました。'
#@@range_end(list4)


#@@range_begin(list5)
class QuitCommand:
    def execute(self):
        sys.exit()  # <1>
#@@range_end(list5)
