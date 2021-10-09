import re


def remove_spaces(query):  # <1>
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def normalize(query):  # <2>
    query = query.casefold()
    return query


if __name__ == '__main__':
    search_query = input('検索文字列を入れてください：')  # <3>
    search_query = remove_spaces(search_query)  # <4>
    search_query = normalize(search_query)
    print(f'次の文字列を検索します："{search_query}"')  # <5>
