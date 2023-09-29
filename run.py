import sys, os
from lib.game import Game
from lib.user_interface import UserInterface
from time import sleep


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)

clear = lambda: os.system('clear')


io = TerminalIO()
p1 = Game()
p2 = Game()
ui1 = UserInterface(io, p1, 'Player 1')
ui2 = UserInterface(io, p2, 'Player 2')
ui1.run()
clear()
ui2.run()
clear()

while p1.lives > 0 and p2.lives > 0:
    ui1._prompt_for_shot(ui2)
    clear()
    if p2.lives == 0:
        break
    ui2._prompt_for_shot(ui1)
    clear()

if p1.lives == 0:
    print("Player 2 wins!")
else:
    print("Player 1 wins!")

sleep(3)