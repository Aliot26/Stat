import reports as r
game_stat_file = "game_stat.txt"
report_file = 'part2/report.txt'

dict_fuction = {
    1: r.get_most_played,
    2: r.sum_sold,
    3: r.get_selling_avg,
    4: r.count_longest_title,
    5: r.get_date_avg,
    6: r.get_game,
    7: r.count_grouped_by_genre,
    8: r.get_date_ordered
}


def main():
    with open(report_file, 'w') as file:
        for key in dict_fuction.keys():
            if key == 6:
                title = input("Print title of the game: ")
                result = dict_fuction[key](game_stat_file, title)
            else:
                result = dict_fuction[key](game_stat_file)
            write_result_to_file(file, result)


def write_result_to_file(file, result):
    result = str(result)
    result = result + '\n'
    file.write(result)


main()
