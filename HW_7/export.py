<<<<<<< HEAD
def export(extension):
    with open('calendar.txt', 'r') as data:
        d = data.readlines()
        for line in d:
            with open(f'temp.{extension}', 'w') as file:
=======
def export(extension):
    with open('calendar.txt', 'r') as data:
        d = data.readlines()
        for line in d:
            with open(f'temp.{extension}', 'w') as file:
>>>>>>> 5cf3acd2959bb64e0335d081736d2c8eff996466
                file.write(line)