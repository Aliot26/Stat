import re
file_name = "game_stat.txt"


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        f = f.read().split('\n')
        f.pop()
        list_games = list(
            list(item for item in element.split('\t') if item) for element in f)
        return list_games


def sort_list(list_something):
    sorted_list = []
    while list_something:
        sorted_list += [list_something.pop(
            list_something.index(min(list_something)))]
    return sorted_list


def list_from_column(table, column_number):
    list_something = []
    for element in table:
        if element[column_number-1]:
            list_something.append(element[column_number-1])
    return list_something


def get_most_played(file_name):
    list_games = read_from_file(file_name)
    list_sold = list_from_column(list_games, 2)
    max_sold = max(float(item) for item in list_sold)
    max_sold = int(max_sold)
    max_sold = str(max_sold)
    for element in list_games:
        if max_sold == element[1]:
            title_of_max_sold = element[0]
    return title_of_max_sold


def sum_sold(file_name):
    list_games = read_from_file(file_name)
    list_sold = list_from_column(list_games, 2)
    count = 0
    for element in list_sold:
        element = float(element)
        count += element
    return count


def get_selling_avg(file_name):
    list_games = read_from_file(file_name)
    sum_sold_games = sum_sold(file_name)
    selling_avg = sum_sold_games/len(list_games)
    return selling_avg


def count_longest_title(file_name):
    list_games = read_from_file(file_name)
    list_title = list_from_column(list_games, 1)
    list_title = sorted(list_title, key=len)
    longest_title = list_title[-1:]
    longest_title = '\t'.join(str(a) for a in longest_title)
    lenght_title = len(longest_title)
    return lenght_title


def get_date_avg(file_name):
    list_games = read_from_file(file_name)
    list_year = list_from_column(list_games, 3)
    sum_years = 0
    for element in list_year:
        element = float(element)
        sum_years += element
    date_avg = int(round(sum_years/len(list_year), 0))
    return date_avg


def get_game(file_name, title):
    list_games = read_from_file(file_name)
    game_output = []
    for element in list_games:
        if title == element[0]:
            game_output.append(element[0])
            game_output.append(float(element[1]))
            game_output.append(int(element[2]))
            game_output.append(element[3])
            game_output.append(element[4])
    if not game_output:
        message_error = 'Game with such title ' + title + ' is not found'
        game_output.append(message_error)

    return game_output


def count_grouped_by_genre(file_name):
    list_games = read_from_file(file_name)
    list_genre = list_from_column(list_games, 4)
    list_genre1 = []
    for item in list_genre:
        item = str(item)
        item = item.lower()
        list_genre1.append(item)
    list_genre = sorted(list_genre, key=lambda v: v.upper())
    dict_count_games_in_genre = {}
    for item in list_genre:
        count = 0
        for element in list_games:
            if item == element[3]:
                count += 1
        dict_count_games_in_genre[item] = count
    return dict_count_games_in_genre


def get_date_ordered(file_name):
    list_games = read_from_file(file_name)
    for element in list_games:
        element[2] = int(element[2])
    list_games.sort(key=lambda k: (-k[2], k[0]), reverse=False)
    list_title = list_from_column(list_games, 1)
    return list_title
