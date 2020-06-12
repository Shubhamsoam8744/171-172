# Write a program that lists all ways people can line up for a photo (all permutations of a list of strings). The program will read a list of one word names, then use a recursive method to create and output all possible orderings of those names, one ordering per line.
#
# When the input is:
#
# Julia Lucas Mia
# then the output is (must match the below ordering):
#
# Julia Lucas Mia
# Julia Mia Lucas
# Lucas Julia Mia
# Lucas Mia Julia
# Mia Julia Lucas
# Mia Lucas Julia

def all_permutations(permList, nameList):
    # TODO: Implement method to create and output all permutations of the list of names.
    if nameList == None or len(nameList) == 0:
        for i in permList:
            print(i, end=" ")
        print()
    else:
        for i in range(len(nameList)):
            permItem = [nameList[i]]
            remItems = nameList[:i] + nameList[i + 1:]
            all_permutations(permList + permItem, remItems)

if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    all_permutations(permList, nameList)
