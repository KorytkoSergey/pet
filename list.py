def check_name_of_the_city(name_of_the_city): #номинальная проверка на правльность названия города(0 - нет, 1 - да)
    check = 1
    if name_of_the_city.isalpha() == True:
        replay = set()
        count_ch = 0
        if name_of_the_city.startswith('ъ') == True or name_of_the_city.startswith('ь') == True or name_of_the_city.startswith('ы') == True:
            check = 0
            return check  # город не может начинаться с ъ, ы, ь
        for character in name_of_the_city:
            if 65 <= ord(character) <= 122: #исключаем латинские буквы и некоторые символы
                check = 0
                return check
            replay.add(character)
            if character == 'й' or character == 'ъ' or character == 'ы' or character == 'ь':
                count_ch += 1
        if count_ch >= 2:
            check = 0
            return check #велика вероятность, что такого города с двумя й, ъ, ы, ь не существует
        if len(replay) == 1:
            check = 0
            return check #города не имееют название из одной/одинаковых буквы/букв
    else:
        check = 0
        return check #название не может из не букв
    return check