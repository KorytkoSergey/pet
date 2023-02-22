# -*- coding: utf-8 -*-
def check_chr(city1, city2):
    flag = False
    while flag == False:
        if city1[-1] == city2[0]:
            flag = True
        else:
            break
    return print(flag)

check_chr('мамама', 'амамамама')


turn_bot = lst_towns[random.randrange(len(lst_towns))]
        test_bot = check_chr(turn_bot, turn_player)



def save_lst_towns(): # добавляет новые города в goroda.txt
    with open("C://Users//apple//PycharmProjects//City//goroda1.txt", 'a') as file:
        new_lst = add_lst_towns
        for i in new_lst:
            file.write('\n')
            file.write(i + '\n')

def add_lst_towns(town): # функция добавления новых городов в общий список, для дальнейшего перезаписывания файла goroda.txt
    new_lst_towns = []
    new_lst_towns.append(town)
    return new_lst_towns

    step_lng = True
    while step_lng == True:
        for letter in step:
            if 1040 <= ord(letter) <= 1103:
                break
            else:
                restep = input('К сожалению, я понимаю, только кирилицу. Прошу вас ввести "Я", "Ты" или "Случайный выбор"')


def the_end_game(flag): #функция заввершения игры
    if flag == 0:
        return print('Кажется я не знаю больше городов, ты победил')
    elif flag == 1:
        return print('Кажется, победа осталось за мной :)')
