import re


def remove_spaces(query):
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def normalize(query):
    query = query.casefold()
    return query

#@@range_begin(list1)
def remove_quotes(query):  # <1>
    query = re.sub(r'"', '', query)
    return query


#@@range_begin(list2)
if __name__ == '__main__':
    search_query = input('検索文字列を入れてください：')
    search_query = remove_spaces(search_query)
    search_query = remove_quotes(search_query)  # <2>
    search_query = normalize(search_query)
    print(f'次の文字列を検索します："{search_query}"')
#@@range_end(list2)    
#@@range_end(list1)
