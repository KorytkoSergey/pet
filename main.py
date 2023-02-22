import random


def create_lst_towns():  # создание списка городов
    with open("goroda.txt", 'r') as file:
        towns1 = list(map(lambda line: line.strip(), file.readlines()))
        towns = []
        for i in towns1:  #отсев пропусков и пробелов в списке
            if i == '' or i == ' ':
                continue
            else:
                towns.append(i.lower())
        return towns

def name_guest(): # функция знакомства
    name = input('Предлагаю сыграть тебе в "Города". Скажи, как тебя зовут?\n')
    print('Привет,', name, 'Если готов, то поехали :)')
    return

def first_step(): #функция выбора первого хода
    step = input('В игре важно, кто начнет. Поэтому, я хочу спросить, кто начнет? Подумай и напиши один из вариантов'
                 '"Я", "Ты" или "Случайный выбор"\n').lower()
    if step == 'случайный выбор':
        num = random.randint(0, 1)
        return num
    elif step == 'ты':
        return 0 # вызов функции начала игры, где начинает бот
    elif step == 'я':
        return 1  # вызов функции начала игры, где начинает первый игрок

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

def the_end_game(flag): #функция заввершения игры(пока не понятно как закончить)
    if flag == 0:
        return print('Кажется я не знаю больше городов, ты победил')
    elif flag == 1:
        return print('Кажется, победа осталось за мной :)')

def base_game():  #основная функция игры
    lst_towns = list(create_lst_towns())
    choice = first_step()
    if choice == 1: # игра начинается с хода игрока
        flag = 0 # флаг на завершение игры(пока не умеем завершать правильно)
        while len(lst_towns) != 0:
            turn_player = input('Твой ход\n').lower() #ход игрока
            solution = check_name_of_the_city(turn_player) #номинальная проверка на адекватное название города
            if solution == 0: #проверка не прошла
                while solution == 0:
                    print('Я думаю, что такого города не существует. Это даже не название города, ты можешь написать настоящее название города?')
                    turn_player = input('Попробуй еще раз\n').lower()
                    solution = check_name_of_the_city(turn_player)
            if turn_player in lst_towns: # проверяем наличие города, который ввел игкрок. Если он в списке, то удаляем.
                position2 = lst_towns.index(turn_player)
                del lst_towns[position2]
            turn_bot = '' #ход бота
            for i in lst_towns:
                step_alpha = 1
                a = turn_player[-1]
                if a == 'й' or a == 'ъ' or a == 'ы' or a == 'ь': #проверка на последнюю букву
                    a = turn_player[-(1 + step_alpha)]
                if i.startswith(a) == True: #из списка городов, достаем город, который начинается с нужной буквы
                    turn_bot = i
                    break
                else:
                    continue
            position1 = lst_towns.index(turn_bot)
            print(turn_bot.title())
            del lst_towns[position1] #удаляем названый город из списка
        return
    if choice == 0: # игра начинается с хода бота
        first_turn_bot = lst_towns[random.randrange(len(lst_towns))] #первый ход бота, случайно определяем первый город из списка
        first_position1 = lst_towns.index(first_turn_bot)
        print(first_turn_bot.title())
        del lst_towns[first_position1] # удаляем названый город
        while len(lst_towns) != 0: # основной ход игры
            turn_player = input('Твой ход\n').lower() #ход игрока
            solution = check_name_of_the_city(turn_player)  # номинальная проверка на адекватное название города
            if solution == 0:  # проверка не прошла
                while solution == 0:
                    print(
                        'Я думаю, что такого города не существует. Это даже не название города, ты можешь написать настоящее название города?')
                    turn_player = input('Попробуй еще раз\n').lower()
                    solution = check_name_of_the_city(turn_player)
            if turn_player in lst_towns:
                position2 = lst_towns.index(turn_player)
                del lst_towns[position2]
            turn_bot = '' #ход бота
            for i in lst_towns:
                step_alpha = 1
                a = turn_player[-1]
                if a == 'й' or a == 'ъ' or a == 'ы' or a == 'ь': #проврека на последнюю букву
                    a = turn_player[-(1 + step_alpha)]
                if i.startswith(a) == True:
                    turn_bot = i
                    break
                else:
                    continue
            position1 = lst_towns.index(turn_bot)
            print(turn_bot.title())
            del lst_towns[position1]
        return

name_guest()
base_game()