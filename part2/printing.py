import reports as r
file_name = "game_stat.txt"

dict_questions = {
    1: "What is the title of the most played game (i.e. sold the most copies)? ",
    2: "How many copies have been sold total? ",
    3: "What is the average selling? ",
    4: "How many characters long is the longest title? ",
    5: "What is the average of the release dates? ",
    6: "What ** properties has a game? ",
    7: "How many games are there grouped by genre? ",
    8: "What is the date ordered list of the games? "
}

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
    print("Hello, Judy! ")
    print('')
    while True:
        output_questions()
        print('')
        number = input_number_question()
        print('')
        print(call_function_by_number(number))
        print('')


def output_questions():
    for key, value in dict_questions.items():
        print(key, ". ", value)
    print("If you want exit print zero.")


def input_number_question():
    try:
        number = int(input("Choose question: "))
    except TypeError:
        print("This is not a number")
    return number


def call_function_by_number(number):
    if number == 0:
        print("Good bye, Judy!")
        exit()
    if number not in dict_fuction:
        print("Question with such number is not exists.")
        exit()
    print(dict_questions[number])
    if number == 6:
        title = input("Print title of the game: ")
        return dict_fuction[number](file_name, title)
    return dict_fuction[number](file_name)


main()
