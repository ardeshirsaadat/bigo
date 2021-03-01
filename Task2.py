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
user_info_dict = {}
max_duration = 0
for call_info in calls:
    # print(call_info[3])
    if int(call_info[3]) > max_duration:
        user_info_dict['calling_tel'] = call_info[0]
        user_info_dict['answering_tel'] = call_info[1]
        user_info_dict['date'] = call_info[2]
        user_info_dict['duration'] = int(call_info[3])
        max_duration = user_info_dict['duration']
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    user_info_dict['answering_tel'], user_info_dict['duration']))
