import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def get_middle(min, max):
    n = round((max + min) / 2)
    if n == min:
        return n + 1
    elif n == max:
        return n - 1
    return n


def game_core_v3(number):
    '''Binary search'''
    count = 0
    min_n = 0
    max_n = 101
    guess = -1
    while number != guess:
        guess = get_middle(min_n, max_n)
        count += 1
        if number > guess:
            min_n = guess
        elif number < guess:
            max_n = guess
    return count  # выход из цикла, если угадали


# запускаем
score_game(game_core_v1)
# Проверяем
score_game(game_core_v2)
# Проверяем
score_game(game_core_v3)
