# Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).
#
# Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating multiple TV shows associated with the same key with a semicolon (;). Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.
#
# Ex: If the input is:
#
# file1.txt
# and the contents of file1.txt are:
#
# 20
# Gunsmoke
# 30
# The Simpsons
# 10
# Will & Grace
# 14
# Dallas
# 20
# Law & Order
# 12
# Murder, She Wrote
# the file output_keys.txt should contain:
#
# 10: Will & Grace
# 12: Murder, She Wrote
# 14: Dallas
# 20: Gunsmoke; Law & Order
# 30: The Simpsons
# and the file output_titles.txt should contain:
#
# Dallas
# Gunsmoke
# Law & Order
# Murder, She Wrote
# The Simpsons
# Will & Grace
# Note: There is a newline at the end of each output file, and file1.txt is available to download.

# FILE MANAGEMENT HATE IS REAL
file_open = input()
count = 0
film_list = ''
season_list = []
new_dict = {}
with open(file_open, 'r') as to_dict:
    for line in to_dict:
        film_read = to_dict.readline()
        film_list += film_read
        try:
            line = int(line)
            season_list.append(line)
        except ValueError:
            continue
    film_list = film_list.split('\n')
    film_list = list(film_list[:-1])
    print(season_list)
    print(film_list)
for num in range(len(season_list)):
    try:
        if season_list[num] in new_dict.keys():
            val_lol = new_dict[season_list[num]]
            same_season = '; ' + str(film_list[num])
            same_season = str(val_lol) + same_season
            new_dict.update({season_list[num]: same_season})
        else:
            new_dict.update({season_list[num]: film_list[num]})
    except IndexError:
        break
new_dict = sorted(new_dict.items())
with open("output_titles.txt", 'w+') as out_titles:
    film_list = sorted(film_list)
    for title in film_list:
        out_titles.write(title)
        out_titles.write("\n")

with open("output_keys.txt", 'w+') as out_key:
    for x, i in new_dict:
        if type(i) == list:
            ##            i = '; '.join(i)
            out_key.write("{}: {}".format(x, i))
        else:
            out_key.write("{}: {}".format(x, i))
        out_key.write("\n")
