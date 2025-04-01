# [] Break start into hour, minute and day part
# [] Break duration into hour, minute


def add_time(start, duration):
    day_part = ''
    new_time = ''
    final_day_part = ''

    add_duration = []
    combine_Time = []
    day_split = []
    start_time = []


    day_split = start.split()
    day_part = day_split.pop()
    start_time = day_split[0].split(':')
    add_duration = duration.split(':')
    if day_part == 'PM':
        start_time[0] = int(start_time[0]) + 12
    combine_Time = [int(start_time[0]) + int(add_duration[0]), int(start_time[1]) + int(add_duration[1])]
    if combine_Time[1] >= 60:
        combine_Time[1] -= 60
        combine_Time[0] += 1
    if combine_Time[0] > 12:
        final_day_part = 'PM'
        combine_Time[0] -= 12
    else: 
        final_day_part = 'AM'

    new_time = f'{combine_Time[0]}:{combine_Time[1]:02d} {final_day_part}'
    return new_time

add_time('11:55 AM', '3:12')