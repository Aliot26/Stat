import reports as r
file_name = "game_stat.txt"

dict_questions = {
    1: "How many games are in the file?",
    2: "Is there a game from a given year?",
    3: "Which was the latest game?",
    4: "How many games do we have by genre?",
    5: "What is the line number of the given game (by title)?",
    6: "What is the alphabetical ordered list of the titles?",
    7: "What are the genres?",
    8: "What is the release date of the top sold 'First-person shooter' game? "
}

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
    if number == 2:
        year = input("Print year: ")
        try:
            year = int(year)
        except TypeError:
            print("invalid literal int()")
        return dict_fuction[number](file_name, year)
    if number == 4:
        genre = input("Print genre: ")
        return dict_fuction[number](file_name, genre)
    if number == 5:
        title = input("Print title: ")
        return dict_fuction[number](file_name, title)
    return dict_fuction[number](file_name)


main()
