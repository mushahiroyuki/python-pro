#@@range_begin(list1)
def has_long_words(sentence):
    if isinstance(sentence, str):  # <1>
       sentence = sentence.split(' ')

    for word in sentence:  # <2>
        if len(word) > 10:  # <3>
            return True

    return False  # <4>
#@@range_end(list1)

print(has_long_words("This is a nice program."))
print(has_long_words("I love hippopotamuses very much."))
print(has_long_words(["I", "love", "hippopotamuses", "very", "much", "."]))
print(has_long_words(["I", "love", "cats", "very", "much", "."]))
