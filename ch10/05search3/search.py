import re


def remove_spaces(query):
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def normalize(query):
    query = query.casefold()
    return query

#@@range_begin(list1)
def remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


if __name__ == '__main__':
    search_query = input('検索文字列を入れてください：')
    search_query = remove_spaces(search_query)  # <1>
    search_query = remove_quotes(search_query)  # <2>
    search_query = normalize(search_query)  # <3>
    print(f'次の文字列を検索します："{search_query}"')

#@@range_end(list1)
