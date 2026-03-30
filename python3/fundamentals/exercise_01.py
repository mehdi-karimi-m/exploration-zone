from pprint import pprint
from timeit import timeit
#return the most repeted character.

user_input = input("Enter something: ")

most_repeted_key, count_of_repeted = ('a', 0)
char_frequency = dict()
for c in user_input:
    if c in char_frequency:
        char_frequency[c] += 1
    else:
        char_frequency[c] = 1

    if count_of_repeted < char_frequency[c]:
        count_of_repeted = char_frequency[c]
        most_repeted_key = c

print(most_repeted_key)

char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse= True)
pprint(char_frequency_sorted)