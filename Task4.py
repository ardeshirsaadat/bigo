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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
"""
musts
answering_call_tel = 0
sending_text_tel=0
receiving_text_tell=0
"""
answering_call_tel = [call[1] for call in calls]
sending_text_tel = [text[0] for text in texts]
receiving_text_tel = [text[1] for text in texts]
numbers_to_exclude = [*answering_call_tel,
                      *sending_text_tel, *receiving_text_tel]
possible_telemarketer_numbers = []
for call in calls:
    if call[0] not in numbers_to_exclude:
        possible_telemarketer_numbers.append(call[0])
print("These numbers could be telemarketers: ")
for number in possible_telemarketer_numbers:
    print(number)
