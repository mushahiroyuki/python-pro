#!/usr/bin/env python

import os
from collections import OrderedDict

import commands


def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print('\t'.join(
            str(field) if field else ''
            for field in bookmark
        ))

        
#@@range_begin(list1)
class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name  # <1>
        self.command = command  # <2>
        self.prep_call = prep_call  # <3>

    def _handle_message(self, message):
        if isinstance(message, list):
            print_bookmarks(message)
        else:
            print(message)

    def choose(self):  # <4>
        data = self.prep_call() if self.prep_call else None  # <5>
        message = self.command.execute(data) if data else self.command.execute()  # <6>
        self._handle_message(message)

    def __str__(self):  # <7>
        return self.name
#@@range_end(list1)


#@@range_begin(list6)
def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
#@@range_end(list6)


#@@range_begin(list2)
def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()
#@@range_end(list2)


#@@range_begin(list4)  6.13
def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options  # <1>


def get_option_choice(options):
    choice = input('操作を選択してください: ')  # <2>
    while not option_choice_is_valid(choice, options):  # <3>
        print('A, B, T, D, Qのいずれかを入力してください（小文字でもOK。ただし半角文字）')
        choice = input('操作を選択してください: ')
    return options[choice.upper()]  # <4>
#@@range_end(list4)


#@@range_begin(list5)
def get_user_input(label, required=True):  # <1>
    value = input(f'{label}: ') or None  # <2>
    while required and not value:  # <3>
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():  # <4>
    return {
        'title': get_user_input('タイトル'),
        'url': get_user_input('URL'),
        'notes': get_user_input('メモ', required=False),  # <5>
    }


def get_bookmark_id_for_deletion():  # <6>
    return get_user_input('削除するブックマークのIDを指定')
#@@range_end(list5)


def loop():  # <1>
    clear_screen()
#@@range_begin(list3)
    options = OrderedDict({
        'A': Option('追加', commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
        'B': Option('登録順にリスト', commands.ListBookmarksCommand()),
        'T': Option('タイトル順にリスト', commands.ListBookmarksCommand(order_by='title')),
        'D': Option('削除', commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
        'Q': Option('終了', commands.QuitCommand()),
    })
    print_options(options)
#@@range_end(list3)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input('Enterを押すとメニューに戻ります')  # <2>


if __name__ == '__main__':
    print("ブックマーク管理アプリ Bark")
    commands.CreateBookmarksTableCommand().execute()

    while True:  # <3>
        loop()
