# -*- coding: utf-8 -*-

import random


def create_lst_towns():  # создание списка городов
    with open("goroda.txt", 'r') as file:
        towns1 = list(map(lambda line: line.strip(), file.readlines()))
        towns = []
        for i in towns1:  # отсев пропусков и пробелов в списке
            if i == '' or i == ' ':
                continue
            else:
                towns.append(i.lower())
        return towns


def name_guest():  # функция знакомства
    name = input('Предлагаю сыграть тебе в "Города". Скажи, как тебя зовут?\n')
    print('Привет,', name, 'Если готов, то поехали :)')
    return


def first_step():  # функция выбора первого хода
    step = input('В игре важно, кто начнет. Поэтому, я хочу спросить, кто начнет? Подумай и напиши один из вариантов'
                 ' "Я", "Ты" или "Случайный выбор"\n').lower()
    dict_ch = {'ты': first_step_by_bot(), 'я': first_step_by_player()}
    if step == 'случайный выбор':
        coin = random.choice(0, 1)
        if coin == 0:
            return first_step_by_bot()  # вызов функции начала игры, где начинает бот
        else:
            return first_step_by_player()  # вызов функции начала игры, где начинает первый игрок
    return dict_ch[step]


def check_name_of_the_city(name_of_the_city):  # номинальная проверка на правильность названия города(0 - нет, 1 - да)
    check = 1
    if name_of_the_city.isalpha():
        not_allowed_letters = 'ъыь'
        replay = set()
        count_ch = 0
        for item in not_allowed_letters:  # проверяем первую букву
            if name_of_the_city.startswith(item):
                check = 0
                return check  # город не может начинаться с ъ, ы, ь
        for character in name_of_the_city:
            if 65 <= ord(character) <= 122:  # исключаем латинские буквы и некоторые символы
                check = 0
                return check
            replay.add(character)
            if any(letter in not_allowed_letters for letter in name_of_the_city):  # проверяем на запрещенные буквы
                count_ch += 1
        if count_ch >= 2:
            check = 0
            return check  # велика вероятность, что такого города с двумя й, ъ, ы, ь не существует
        if len(replay) == 1:
            check = 0
            return check  # города не имеют название из одной/одинаковых буквы/букв
    else:
        check = 0
        return check  # название не может из не букв
    return check


def fresh(name):  # функция проверки, есть данное название в списке, если нет - добавляем в список не известных городов
    point = 1
    lst_of_towns = create_lst_towns()
    if name not in lst_of_towns:
        point = 0  # такого города в списке нет
    return point


list_of_the_new_cities = []  # список новых городов, которые потом будут добавлены в основной список файла goroda.txt


def the_end_game(flag):  # функция завершения игры(пока не понятно как закончить)
    if flag == 0:
        return print('Кажется я не знаю больше городов, ты победил')
    elif flag == 1:
        return print('Кажется, победа осталось за мной :)')

# city - передаваемая переменная, в которой должен храниться список городов.
# Он должен постоянно уменьшаться, поэтому его и передаем из функции в функцию. Но что-то идет не так.


def list_of_towns(town, city):  # принимаем город, обрабатываем и удаляем его из списка. Не удаляет :(
    lst_towns = city
    if town in lst_towns:  # Проверяем наличие города, который ввел игрок. Если он в списке, то удаляем.
        position = lst_towns.index(town)
        del lst_towns[position]
    if fresh(town) == 0:  # 0 после проверки, это значит название не знакомо и вносим в новый список(??)
        list_of_the_new_cities.append(town)
    return lst_towns


def first_step_by_player():  # первый ход игрока
    step_player = input('Твой ход\n').lower()
    solution = check_name_of_the_city(step_player)  # номинальная проверка на адекватное название города
    if solution == 0:  # проверка не прошла
        while solution == 0:
            print('Я думаю, что такого города не существует. Ты можешь написать настоящее название города?')
            step_player = input('Попробуй еще раз\n').lower()
            solution = check_name_of_the_city(step_player)
    city = list_of_towns(step_player, create_lst_towns())
    return turn_bot(step_player, city)  # передаем ход боту


def first_step_by_bot():  # первый ход бота
    lst_towns = create_lst_towns()
    first_turn_bot = lst_towns[random.randrange(len(lst_towns))]  # случайно определяем первый город из списка
    city = list_of_towns(first_turn_bot, create_lst_towns())
    print(first_turn_bot.title())
    return turn_player(first_turn_bot, city)  # передаем ход игроку


def turn_player(step_bot, city):  # ход игрока
    flag = 0
    step_player = None
    while flag == 0:  # проверка на первая-последня буква
        a = step_bot[-1]
        step_alpha = 1
        if a == 'й' or a == 'ъ' or a == 'ы' or a == 'ь':  # проверка на последнюю букву
            a = step_bot[-(1 + step_alpha)]
        step_player = input('Твой ход\n').lower()  # выдает глюк с ходом, если написать неверный город
        if step_player[0] != a:
            print('Первая буква твоего названия, должна совпадать с последней буквой предыдущего названия.')
            step_player = input('Попробуй еще раз\n').lower()
            solution = check_name_of_the_city(step_player)  # номинальная проверка на адекватное название города
            if solution == 0:  # проверка не прошла
                while solution == 0:
                    print('Я думаю, что такого города не существует. Ты можешь написать настоящее название города?')
                    step_player = input('Попробуй еще раз\n').lower()
                    solution = check_name_of_the_city(step_player)
            flag = 0
        else:
            flag = 1
    city_player = list_of_towns(step_player, city)
    return turn_bot(step_player, city_player)  # передаем ход боту


def turn_bot(step_player, city):  # ход бота
    lst_towns = create_lst_towns()
    step_bot = None
    for i in lst_towns:
        step_alpha = 1
        a = step_player[-1]
        if a == 'й' or a == 'ъ' or a == 'ы' or a == 'ь':  # проверка на последнюю букву
            a = step_player[-(1 + step_alpha)]
        if i.startswith(a):  # из списка городов, достаем город, который начинается с нужной буквы
            step_bot = i
            break
        else:
            continue
    city_bot = list_of_towns(step_bot, city)
    print(step_bot.title())
    return turn_player(step_bot, city_bot)  # передаем ход игроку


name_guest()
first_step()
