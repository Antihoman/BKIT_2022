from operator import itemgetter
from math import inf


class Program:

    def __init__(self, id, language, length, computer_id):
        self.id = id
        self.language = language
        self.length = length
        self.computer_id = computer_id


class Computer:

    def __init__(self, id, frame):
        self.id = id
        self.frame = frame


class ProgramComp:

    def __init__(self, computer_id, program_id):
        self.computer_id = computer_id
        self.program_id = program_id


# Компьютеры
computers = [
    Computer(1, 'Plastic white frame'),
    Computer(2, 'Metal pink frame'),
    Computer(3, 'flint yellow frame'),

    Computer(11, 'Metal black frame'),
    Computer(22, 'Metal red frame'),
    Computer(33, 'Plastic black frame'),
]

# Програмы
programs = [
    Program(1, 'C++', 1000, 1),
    Program(2, 'Python', 500, 2),
    Program(3, 'C', 400, 3),
    Program(4, 'C++', 2000, 3),
    Program(5, 'Python', 100, 3),
]

programs_comps = [
    ProgramComp(1, 1),
    ProgramComp(2, 2),
    ProgramComp(3, 3),
    ProgramComp(3, 4),
    ProgramComp(3, 5),

    ProgramComp(11, 1),
    ProgramComp(22, 2),
    ProgramComp(33, 3),
    ProgramComp(33, 4),
    ProgramComp(33, 5),
]


def print_by_line(data):
    for line in data:
        print(line)


def task_1(one_to_many):
    """«Программа» и «Компьютер» связаны соотношением один-ко-многим. Выведите список всех программ, Ккоторые \
    написаны на языке Python, и корпусов компьютера."""
    print('Задание B1')
    print_by_line([(record[0], record[2]) for record in one_to_many if record[0].startswith('Python')])


def task_2(one_to_many):
    """«Программа» и «Компьютер» связаны соотношением один - ко - многим.Выведите список компьютеров с минимальной \
    длинной программ кода, отсортированный по минимальной длинне."""
    print('\nЗадание B2')
    mins = {}
    for language, length, processor in one_to_many:
        mins[processor] = min(mins.get(processor, inf), length)
    print_by_line(sorted(mins.items(), key=itemgetter(1)))


def task_3(many_to_many):
    """«Программа» и «Компьютер» связаны соотношением многие-ко-многим. Выведите список всех связанных программ и компьютеров,\
    отсортированный по программам, сортировка по компьютерам произвольная. """
    print('\nЗадание B3')
    print_by_line(sorted(many_to_many, key=itemgetter(1)))


def main():

    # Соединение данных один-ко-многим
    one_to_many = [(program.language, program.length, computer.frame)
                   for program in programs
                   for computer in computers
                   if program.computer_id == computer.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(computer.frame, programs_c.computer_id, programs_c.program_id)
                         for computer in computers
                         for programs_c in programs_comps
                         if computer.id == programs_c.computer_id]

    many_to_many = [(program.language, program.length, processor)
                    for processor, computer_id, program_id in many_to_many_temp
                    for program in programs
                    if program.id == program_id]

    task_1(one_to_many)
    task_2(one_to_many)
    task_3(many_to_many)


if __name__ == '__main__':
    main()