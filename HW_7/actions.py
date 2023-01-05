<<<<<<< HEAD
file = 'calendar.txt'


def write_event(day, time, event):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('\n {} {} - {}'.format(day, time, event))

def show_calendar():
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
=======
file = 'calendar.txt'


def write_event(day, time, event):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('\n {} {} - {}'.format(day, time, event))

def show_calendar():
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
>>>>>>> 5cf3acd2959bb64e0335d081736d2c8eff996466
            print(line)