"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def count_unrepeated_numbers(list_of_numbers):
    set_count = set()
    for number in list_of_numbers:
        set_count.add(number)
    return len(set_count)


def extract_numbers(list):
    numbers = [list_of_text[0:2] for list_of_text in list]
    list_numbers = []
    for number in numbers:
        for num in number:
            list_numbers.append(num)
    return list_numbers


print("There are {} different telephone numbers in the records.".format(
    count_unrepeated_numbers([*extract_numbers(texts), *extract_numbers(calls)])))
