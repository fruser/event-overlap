import csv
from _datetime import datetime
import sys


def get_timestamp(date_time_str):
    # if empty return 2030-01-01::00:00
    date_time_str = date_time_str.strip()
    return int(datetime.strptime(date_time_str, '%Y-%m-%d::%H:%M').timestamp()) if date_time_str else 1893474000


def get_reverse_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d::%H:%M')


def am_i_double_booked(csv_file):
    working_set = {}
    overlap = []

    with open(csv_file) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            start = get_timestamp(row[0])
            end = get_timestamp(row[1])

            # offset start time by 1min
            meeting = set(range(start + 60, end, 60))

            for event in working_set:
                result = working_set[event].intersection(meeting)

                if result:
                    # overlap found, capture as `meeting_a | meeting_b`
                    overlap.append('{0} - {1} | {2} - {3}'.format(
                        get_reverse_timestamp(event[0]),
                        get_reverse_timestamp(event[1]),
                        get_reverse_timestamp(start),
                        get_reverse_timestamp(end)
                    ))

            working_set[(start, end)] = meeting

    return overlap


def main(sys_args):
    schedule = sys_args[1] if len(sys_args) > 1 else './csv/schedule.csv'

    overlaps = am_i_double_booked(schedule)
    if not overlaps:
        print("Good, don't have any overlaps...")
    else:
        print("Ops, I'm being double booked")
        for event in overlaps:
            print(event)


if __name__ == '__main__':
    main(sys.argv)
