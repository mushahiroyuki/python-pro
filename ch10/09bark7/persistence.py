from abc import ABC, abstractmethod

from database import DatabaseManager


class PersistenceLayer(ABC):  # <1>
    @abstractmethod
    def create(self, data):  # <2>
        raise NotImplementedError('パーシスタンス層では必ずメソッドcreateを実装してください')

    @abstractmethod
    def list(self, order_by=None):
        raise NotImplementedError('パーシスタンス層では必ずメソッドlistを実装してください')

    @abstractmethod
    def edit(self, bookmark_id, bookmark_data):
        raise NotImplementedError('パーシスタンス層では必ずメソッドeditを実装してください')

    @abstractmethod
    def delete(self, bookmark_id):
        raise NotImplementedError('パーシスタンス層では必ずメソッドdeleteを実装してください')


class BookmarkDatabase(PersistenceLayer):  # <3>
    def __init__(self):
        self.table_name = 'bookmarks'  # <4>
        self.db = DatabaseManager('bookmarks.db')

        self.db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'タイトル': 'text not null',
            'URL': 'text not null',
            'メモ': 'text',
            '追加日時': 'text not null',
        })

    def create(self, bookmark_data):  # <5>
        self.db.add(self.table_name, bookmark_data)

    def list(self, order_by=None):
        return self.db.select(self.table_name, order_by=order_by).fetchall()

    def edit(self, bookmark_id, bookmark_data):
        self.db.update(self.table_name, {'id': bookmark_id}, bookmark_data)

    def delete(self, bookmark_id):
        self.db.delete(self.table_name, {'id': bookmark_id})
