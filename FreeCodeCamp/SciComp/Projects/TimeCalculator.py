# [] Break start into hour, minute and day part
# [] Break duration into hour, minute
# [] handle multiple days



def add_time(start, duration):
    day_part = ''
    new_time = ''
    final_day_part = ''
    day_change = ''
    total_days = 0

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
# Minute Handling
    while combine_Time[1] >= 60:
        combine_Time[1] -= 60
        combine_Time[0] += 1

# Day Handling
    while combine_Time[0] >= 24:
        if combine_Time[0] >= 24:
            total_days += 1
            combine_Time[0] -= 24

# Hour Handling
    if combine_Time[0] >= 12:
        final_day_part = 'PM'
        if combine_Time[0] > 12:
            combine_Time[0] -= 12

    else:
        final_day_part = 'AM'
        if combine_Time[0] == 0:
            combine_Time[0] += 12

    if total_days == 1:
        day_change = ' (next day)'
    elif total_days > 1:
        day_change = ' (' + str(total_days) + ' days later)'

    new_time = f'{combine_Time[0]}:{combine_Time[1]:02d} {final_day_part}{day_change}'
    return new_time

print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))