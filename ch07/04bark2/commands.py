import sys
from datetime import datetime

import requests

from database import DatabaseManager

db = DatabaseManager('bookmarks.db')


class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'タイトル': 'text not null',
            'URL': 'text not null',
            'メモ': 'text',
            'date_added': 'text not null',
        })

#@@range_begin(list1)
class AddBookmarkCommand:
    def execute(self, data, timestamp=None):  # <1>
        data['date_added'] = timestamp or datetime.utcnow().isoformat()  # <2>
        db.add('bookmarks', data)
        return 'ブックマークを追加しました。'
#@@range_end(list1)

class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})
        return 'ブックマークを削除しました。'


class QuitCommand:
    def execute(self):
        sys.exit()

#@@range_begin(list2)
class ImportGitHubStarsCommand:
    def _extract_bookmark_info(self, repo):  # <1>
        return {
            'タイトル': repo['name'],
            'URL': repo['html_url'],
            'メモ': repo['description'],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data['github_username']
        next_page_of_results = \
            f'https://api.github.com/users/{github_username}/starred'  # <2>

        while next_page_of_results:  # <3>
            stars_response = requests.get(  # <4>
                next_page_of_results,
                headers={'Accept': 'application/vnd.github.v3.star+json'},
            )
            next_page_of_results = stars_response.links.get('next', {}).get('url')  # <5>

            for repo_info in stars_response.json(): # スターごとの繰り返し
                repo = repo_info['repo']  # <6>

                if data['preserve_timestamps']:
                    timestamp = datetime.strptime(
                        repo_info['starred_at'],  # <7>
                        '%Y-%m-%dT%H:%M:%SZ'  # <8>
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(  # <9>
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp,
                )

        return f'{bookmarks_imported}個のブックマークをインポートしました。'  # <10>
#@@range_end(list2)
