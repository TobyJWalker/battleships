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
clear()

while p1.lives > 0 and p2.lives > 0:
    '''
    create a function in ui to display the hit grid
    create a function in ui to prompt for a shot
    create a function to check if that coordinate has been shot at before and not out of bounds
    create a separate functions in ui to handle the shot (such as check for hit miss, update hit grid, increment hit counter)

    '''
    ui1._prompt_for_shot(ui2)
    clear()
    ui2._prompt_for_shot(ui1)
    clear()

'''
Check who still has lives and declare them the winner
'''