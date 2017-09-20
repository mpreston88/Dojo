from datetime import datetime
import pprint


def convert3ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

fts = {convert3ampm(k): v.title() for k, v in flights.items()}

when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}


pprint.pprint(when)

