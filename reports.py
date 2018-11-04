# Report functions
#import sys
from operator import itemgetter


file_name = "game_stat.txt"
year = 2000
genre = 'RPG'
title = 'StarCraft'


def main():
    '''print(count_games(file_name))
    t = decide(file_name, year)
    print(t)
    get_latest(file_name)
    print(get_latest(file_name))
    print(count_by_genre(file_name, genre))
    print(get_line_number_by_title(file_name, title))
    print(sort_abc(file_name))
    print(get_genres(file_name))'''
    when_was_top_sold_fps(file_name)


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        f = f.read().split('\n')
        f.pop()
        list_games = list(
            list(item for item in element.split('\t') if item) for element in f)
        return list_games


def list_from_column(table, column_number):
    list_something = []
    for element in table:
        if element[column_number-1]:
            list_something.append(element[column_number-1])
    return list_something


def sort_list(list_something):
    sorted_list = []
    while list_something:
        sorted_list += [list_something.pop(
            list_something.index(min(list_something)))]
    return sorted_list


def count_games(file_name):
    list_games = read_from_file(file_name)
    return len(list_games)


def decide(file_name, year):
    list_games = read_from_file(file_name)
    year = str(year)
    for element in list_games:
        for item in element:
            if year == item:
                return True
    return False


def get_latest(file_name):
    list_games = read_from_file(file_name)
    max_year_game = max(list_games, key=itemgetter(2))[0]
    return max_year_game


def count_by_genre(file_name, genre):
    list_games = read_from_file(file_name)
    count = 0
    for element in list_games:
        if genre in element:
            count += 1
    if count == 0:
        count = 'Game with such genre ' + genre + ' is not found'
    return count


def get_line_number_by_title(file_name, title):
    list_games = read_from_file(file_name)
    i = 0
    for element in list_games:
        if title in list_games[i]:
            ind = i
            break
        i += 1
    return ind+1


def sort_abc(file_name):
    list_games = read_from_file(file_name)
    list_title = list_from_column(list_games, 1)
    sorted_list_title = sort_list(list_title)
    sorted_games_list = []
    for item in sorted_list_title:
        for element in list_games:
            if item == element[0]:
                sorted_games_list.append(element)
    return sorted_list_title


def get_genres(file_name):
    list_games = read_from_file(file_name)
    list_genres = list_from_column(list_games, 4)
    list_genres = set(list_genres)
    list_genres = list(list_genres)
    sorted_list_genres = sort_list(list_genres)
    return sorted_list_genres


def when_was_top_sold_fps(file_name):
    list_games = read_from_file(file_name)
    genre = "First-person shooter"
    list_shooters = []
    for element in list_games:
        for item in element:
            if item == genre:
                list_shooters.append(element)
    list_sold = list_from_column(list_shooters, 2)
    max_sold = max(float(item) for item in list_sold)
    max_sold = str(max_sold)
    for element in list_shooters:
        for item in element:
            if max_sold == element[1] and genre == element[3]:
                year_of_max_sold = element[2]
    return int(year_of_max_sold)


main()
