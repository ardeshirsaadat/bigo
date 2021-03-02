"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
cummulative_call_duration_per_number = {}
for call in calls:
    if call[0] not in cummulative_call_duration_per_number.keys():
        cummulative_call_duration_per_number[call[0]] = int(call[3])
    if call[1] not in cummulative_call_duration_per_number.keys():
        cummulative_call_duration_per_number[call[1]] = int(call[3])
    if call[0] in cummulative_call_duration_per_number.keys():
        cummulative_call_duration_per_number[call[0]] += int(call[3])
    if call[1] in cummulative_call_duration_per_number.keys():
        cummulative_call_duration_per_number[call[1]] += int(call[3])
max_commulative_duration_number = max(
    cummulative_call_duration_per_number, key=cummulative_call_duration_per_number.get)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    max_commulative_duration_number, cummulative_call_duration_per_number[max_commulative_duration_number]))
