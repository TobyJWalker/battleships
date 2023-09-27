import sys, os
from lib.game import Game
from lib.user_interface import UserInterface


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