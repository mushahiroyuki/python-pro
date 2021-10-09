import re


def _remove_spaces(query):  # <1>
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def _normalize(query):
    query = query.casefold()
    return query


def _remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


def clean_query(query):  # <2>
    query = _remove_spaces(query)
    query = _remove_quotes(query)
    query = _normalize(query)
    return query


if __name__ == '__main__':
    search_query = input('検索文字列を入れてください：')
    search_query = clean_query(search_query)  # <3>
    print(f'次の文字列を検索します："{search_query}"')
