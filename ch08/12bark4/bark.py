#!/usr/bin/env python3

import os
from collections import OrderedDict

import commands


def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print('\t'.join(
            str(field) if field else ''
            for field in bookmark
        ))


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def _handle_message(self, message):
        if isinstance(message, list):
            print_bookmarks(message)
        else:
            print(message)

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data)  # <1>
        self._handle_message(message)

    def __str__(self):
        return self.name


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input('操作を選択してください: ')
    while not option_choice_is_valid(choice, options):
        print('A, B, T, E, D, G, Qのいずれかを入力してください（小文字でもOK。ただし半角文字）')
        choice = input('操作を選択してください: ')
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():
    return {
        'タイトル': get_user_input('タイトル'),
        'URL': get_user_input('URL'),
        'メモ': get_user_input('メモ', required=False),
    }


def get_bookmark_id_for_deletion():
    return get_user_input('削除するブックマークのIDを指定')


def get_github_import_options():
    return {
        'github_username': get_user_input('GitHubのユーザー名'),
        'preserve_timestamps':
            get_user_input(
                'タイムスタンプを維持しますか [Y/n]',
                required=False
            ) in {'Y', 'y', None},
    }


def get_new_bookmark_info():
    bookmark_id = get_user_input('編集対象のIDを入力してください')
    field = get_user_input('編集項目を指定してください（「タイトル」「URL」「メモ」のいずれか）')
    new_value = get_user_input(f'{field}の新しい値')
    return {
        'id': bookmark_id,
        'update': {field: new_value},
    }


def loop():
    clear_screen()

    options = OrderedDict({
        'A': Option('追加', commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
        'B': Option('登録順にリスト', commands.ListBookmarksCommand()),
        'T': Option('タイトル順にリスト', commands.ListBookmarksCommand(order_by='タイトル')),
        'E': Option('編集', commands.EditBookmarkCommand(), prep_call=get_new_bookmark_info),
        'D': Option('削除', commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
        'G': Option(
            'GitHubのスターをインポート',
            commands.ImportGitHubStarsCommand(),
            prep_call=get_github_import_options
        ),
        'Q': Option('終了', commands.QuitCommand()),
    })
    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input('Enterを押すとメニューに戻ります')


if __name__ == '__main__':
    print("ブックマーク管理アプリ Bark")
    commands.CreateBookmarksTableCommand().execute()

    while True:
        loop()
