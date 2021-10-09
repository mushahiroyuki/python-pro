import sys
from abc import ABC, abstractmethod
from datetime import datetime

import requests

from database import DatabaseManager

db = DatabaseManager('bookmarks.db')


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError('コマンドは必ずメソッドexecuteを実装してください')


class CreateBookmarksTableCommand(Command):
    def execute(self, data=None):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'タイトル': 'text not null',
            'URL': 'text not null',
            'メモ': 'text',
            '追加日時': 'text not null',
        })


#@@range_begin(list1)
class AddBookmarkCommand(Command):  # <1>
    def execute(self, data, timestamp=None):
        data['追加日時'] = timestamp or datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return True, None  # <2>


class ListBookmarksCommand(Command):  # <3>
    def __init__(self, order_by='追加日時'):
        self.order_by = order_by

    def execute(self, data=None):
        return True, db.select('bookmarks', order_by=self.order_by).fetchall()  # <4>
#@@range_end(list1)


class DeleteBookmarkCommand(Command):
    def execute(self, data):
        db.delete('bookmarks', {'id': data})
        return True, None


class QuitCommand(Command):
    def execute(self, data=None):
        sys.exit()


class ImportGitHubStarsCommand(Command):
    def _extract_bookmark_info(self, repo):
        return {
            'タイトル': repo['name'],
            'URL': repo['html_url'],
            'メモ': repo['description'],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data['github_username']
        next_page_of_results = f'https://api.github.com/users/{github_username}/starred'

        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={'Accept': 'application/vnd.github.v3.star+json'},
            )
            next_page_of_results = stars_response.links.get('next', {}).get('url')

            for repo_info in stars_response.json():
                repo = repo_info['repo']

                if data['preserve_timestamps']:
                    timestamp = datetime.strptime(
                        repo_info['starred_at'],
                        '%Y-%m-%dT%H:%M:%SZ'
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp,
                )

        return True, bookmarks_imported


class EditBookmarkCommand(Command):
    def execute(self, data):
        db.update(
            'bookmarks',
            {'id': data['id']},
            data['update'],
        )
        return True, None
