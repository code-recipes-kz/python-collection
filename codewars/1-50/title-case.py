# tags: Strings, Fundamentals
# kyu: 6

def title_case(title, minor_words=''):
    """
    Преобразовывает строку в заголовочный регистр (title case), с учетом списка исключений (minor words).

    :param title: Исходная строка, которую нужно преобразовать.
    :type title: str
    :param minor_words: Список исключений - слов, которые всегда должны быть в нижнем регистре, за исключением
                        первого слова в строке. По умолчанию None.
    :type minor_words: str or None
    :return: Строка в заголовочном регистре (title case).
    :rtype: str
    """
    if not title:
        return ""

    if not minor_words:
        # Если список исключений (minor words) не предоставлен, просто делаем первую букву каждого слова заглавной
        return " ".join(word.capitalize() for word in title.split())

    # Преобразуем список исключений (minor_words) в нижний регистр и разделяем его на список слов
    minor_words_list = minor_words.lower().split()

    # Делаем первую букву каждого слова заглавной, за исключением слов из списка исключений (minor words)
    title_words = title.split()
    title_case_words = []
    for i, word in enumerate(title_words):
        if i == 0 or word.lower() not in minor_words_list:
            # Делаем первое слово заглавным или слова, которые не находятся в списке исключений (minor words)
            title_case_words.append(word.capitalize())
        else:
            # Преобразуем слово из списка исключений (minor word) в нижний регистр и добавляем как есть
            title_case_words.append(word.lower())

    # Соединяем слова в строку с заглавными буквами
    title_case_string = " ".join(title_case_words)

    return title_case_string
