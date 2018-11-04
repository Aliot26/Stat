import reports as r
file_name = "game_stat.txt"

#dict_questions = {}
print("Hello, Judy! ")
print('')


print("How many games are in the file?")
print(r.count_games(file_name))
print('')

print("Is there a game from a given year?")
year = input("Print year ")
try:
    year = int(year)
except:
    TypeError: ("invalid literal int()")
print(r.decide(file_name, year))
print('')

print("Which was the latest game?")
print(r.get_latest(file_name))
print('')

print("How many games do we have by genre?")
genre = input("Print genre")
print(r.count_by_genre(file_name, genre))
print('')

print("What is the line number of the given game (by title)?")
genre = input("Print title")
print(r.get_line_number_by_title(file_name, title))
print('')

print("What is the alphabetical ordered list of the titles?")
print(r.sort_abc(file_name))
print('')

print("What are the genres?")
print(r.get_genres(file_name))
print('')

print("What is the release date of the top sold 'First-person shooter' game? ")
print(r.when_was_top_sold_fps(file_name))
print('')
