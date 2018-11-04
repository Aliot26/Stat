import reports as r
game_stat_file = "game_stat.txt"
report_file = 'report.txt'

dict_fuction = {
    1: r.count_games,
    2: r.decide,
    3: r.get_latest,
    4: r.count_by_genre,
    5: r.get_line_number_by_title,
    6: r.sort_abc,
    7: r.get_genres,
    8: r.when_was_top_sold_fps
}


def main():
    with open(report_file, 'w') as file:
        for key in dict_fuction.keys():
            if key == 2:
                year = input("Print year: ")
                try:
                    year = int(year)
                except TypeError:
                    print("invalid literal int()")
                result = dict_fuction[key](game_stat_file, year)
            elif key == 4:
                genre = input("Print genre: ")
                result = dict_fuction[key](game_stat_file, genre)
            elif key == 5:
                title = input("Print title: ")
                result = dict_fuction[key](game_stat_file, title)
            else:
                result = dict_fuction[key](game_stat_file)
            write_result_to_file(file, result)


def write_result_to_file(file, result):
    result = str(result)
    result = result + '\n'
    file.write(result)


main()
