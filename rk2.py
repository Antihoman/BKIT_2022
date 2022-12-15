import unittest
from main import Computer, Program, ProgramComp, task_1, task_2, task_3


class TestDB(unittest.TestCase):
    def setUp(self):
        # Компьютеры
        self.computers = [
            Computer(1, 'Plastic white frame'),
            Computer(2, 'Metal pink frame'),
            Computer(3, 'flint yellow frame'),

            Computer(11, 'Metal black frame'),
            Computer(22, 'Metal red frame'),
            Computer(33, 'Plastic black frame'),
        ]

        # Програмы
        self.programs = [
            Program(1, 'C++', 1000, 1),
            Program(2, 'Python', 500, 2),
            Program(3, 'C', 400, 3),
            Program(4, 'C++', 2000, 3),
            Program(5, 'Python', 100, 3),
        ]

        self.programs_comps = [
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
        # Соединение данных один-ко-многим
        self.one_to_many = [(program.language, program.length, computer.frame)
                            for program in self.programs
                            for computer in self.computers
                            if program.computer_id == computer.id]

        # Соединение данных многие-ко-многим
        many_to_many_temp = [(computer.frame, pr_c.computer_id, pr_c.program_id)
                             for computer in self.computers
                             for pr_c in self.programs_comps
                             if computer.id == pr_c.computer_id]
        self.many_to_many = [(program.language, program.length, frame)
                             for frame, computer_id, program_id in many_to_many_temp
                             for program in self.programs
                             if program.id == program_id]

    def test_task_1(self):
        result = set(task_1(self.one_to_many))
        answer = {('Python', 'Metal pink frame'),
                  ('Python', 'flint yellow frame')}
        self.assertEqual(answer, result)

    def test_task_2(self):
        result = task_2(self.one_to_many)
        answer = [('flint yellow frame', 100),
                  ('Metal pink frame', 500),
                  ('Plastic white frame', 1000)]
        self.assertEqual(answer, result)

    def test_task_3(self):
        result = task_3(self.many_to_many)
        answer = [('Python', 100, 'flint yellow frame'),
                  ('Python', 100, 'Plastic black frame'),
                  ('C', 400, 'flint yellow frame'),
                  ('C', 400, 'Plastic black frame'),
                  ('Python', 500, 'Metal pink frame'),
                  ('Python', 500, 'Metal red frame'),
                  ('C++', 1000, 'Plastic white frame'),
                  ('C++', 1000, 'Metal black frame'),
                  ('C++', 2000, 'flint yellow frame'),
                  ('C++', 2000, 'Plastic black frame')]
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
