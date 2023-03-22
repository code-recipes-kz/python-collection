def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    # Первое слово должно начинаться с маленькой буквы, если исходное слово начиналось с маленькой буквы,
    # и с большой буквы, если исходное слово начиналось с большой буквы.
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    return ''.join(camel_case_words)