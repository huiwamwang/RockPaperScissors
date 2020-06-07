from random import choice


class RockPaperScissors:
    name = None

    def __init__(self):
        self.file = open('rating.txt')
        self.options = None
        self.calculations = None
        self.length = None
        self.inp = None
        self.computer_choice = None
        self.print = None
        self.name = None
        self.score = 0
        self.ind = None

    def __str__(self):
        if self.print == 1:
            return f'There is a draw ({self.computer_choice})'
        elif self.print == 2:
            return f'Sorry, but computer chose {self.computer_choice}'
        elif self.print == 3:
            return f'Well done. Computer chose {self.computer_choice} and failed'
        elif self.print == 4:
            return 'Invalid input'
        elif self.print == 5:
            return f'Your rating: {self.score}'

    def action(self, inp):
        self.name = RockPaperScissors.name
        for line in self.file:
            if self.name in line:
                self.score += int(line.split()[1])
        self.inp = inp
        self.computer_choice = choice(self.options)
        if self.inp == '!exit':
            print('Bye!')
            exit()
        self.check()

    def check(self):
        try:
            if self.inp == '!rating':
                self.print = 5
            else:
                self.ind = self.calculations.index(self.inp)
                if self.inp == self.computer_choice:
                    self.print = 1
                    self.score += 50
                elif self.computer_choice in self.calculations[self.ind + 1:self.ind + self.length + 1]:
                    self.print = 2
                elif self.computer_choice in self.calculations[
                                             self.ind + self.length + 1:self.ind + 2 * self.length + 1]:
                    self.print = 3
                    self.score += 100
        except KeyError and ValueError:
            self.print = 4

    def rules(self, inp):
        if len(inp) < 2:
            inp = 'rock,paper,scissors'
        self.options = inp.split(',')
        self.calculations = self.options * 2
        self.length = (len(self.options) - 1) // 2


game = RockPaperScissors()
RockPaperScissors.name = input("Enter your name: > ")
print(f'Hello, {RockPaperScissors.name}')
game.rules(input())
print("Okay, let's start")

while True:
    game.action(input())
    print(game)