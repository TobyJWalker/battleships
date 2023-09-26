from lib.user_interface import *
from unittest.mock import Mock
from lib.game import *

def test_ship_overlap():
    game = Game()
    interface = UserInterface(Mock(), game)
    game.place_ship(length= 3, orientation="horizontal", row=5, col=4)
    assert interface.ship_overlap(5,5) == True
    assert interface.ship_overlap(10,10) == False