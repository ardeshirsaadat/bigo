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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def disintegrate_text_info(texts_list, desired_record):
    incoming_number = texts_list[desired_record][0]
    answering_number = texts_list[desired_record][1]
    timestamp = texts_list[desired_record][2]
    return incoming_number, answering_number, timestamp


def disintegrate_call_info(call_list, desired_record):
    incoming_number = call_list[desired_record][0]
    answering_number = call_list[desired_record][1]
    timestamp = call_list[desired_record][2]
    duration = call_list[desired_record][3]
    return incoming_number, answering_number, timestamp, duration


print("First record of texts, {} texts {} at time {}".format(
    disintegrate_text_info(texts, 0)[0], disintegrate_text_info(texts, 0)[1], disintegrate_text_info(texts, 0)[2]))


print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    disintegrate_call_info(calls, -1)[0], disintegrate_call_info(calls, -1)[1], disintegrate_call_info(calls, -1)[2], disintegrate_call_info(calls, -1)[3]))
