from lib.user_interface import *
from unittest.mock import Mock
from lib.game import *

def test_ship_overlap():
    game = Game()
    interface = UserInterface(Mock(), game)
    game.place_ship(length= 3, orientation="horizontal", row=5, col=4)
    assert interface.ship_overlap(5,5) == True
    assert interface.ship_overlap(10,10) == False

def test_ship_overlap_end_of_ship():
    game = Game()
    interface = UserInterface(Mock(), game)
    game.place_ship(length= 3, orientation="horizontal", row=5, col=4)
    assert interface.ship_overlap(3, 5, 3, 'v') == True
    assert interface.ship_overlap(5, 2, 3, 'h') == True

def test_ship_removed_from_list():
    game = Game()
    interface = UserInterface(Mock(), game)
    game.place_ship(length= 3, orientation="horizontal", row=5, col=4)
    assert interface.unplaced_ships == [Ship(2), Ship(3), Ship(3), Ship(4), Ship(5)]
    interface.start_ship_placement(2, 'h', 5, 4)
    assert interface.unplaced_ships == [Ship(3), Ship(3), Ship(4), Ship(5)]
    interface.start_ship_placement(3, 'h', 6, 4)
    assert interface.unplaced_ships == [Ship(3), Ship(4), Ship(5)]
    interface.start_ship_placement(3, 'h', 7, 4)
    assert interface.unplaced_ships == [Ship(4), Ship(5)]

def test_ui_name():
    interface = UserInterface(Mock(), Mock(), 'Player 1')
    assert interface.name == 'Player 1'

def test_initial_hit_grid():
    interface = UserInterface(Mock(), Mock())
    assert len(interface.hit_grid) == 10
    assert len(interface.hit_grid[0]) == 10
    assert interface.hit_grid[0][0] == '.'

def test_shot_out_of_bounds():
    interface = UserInterface(Mock(), Mock())
    assert interface.check_shot_valid(11, 11, Mock()) == False
    assert interface.check_shot_valid(-1, -1, Mock()) == False

def test_shot_already_taken():
    interface = UserInterface(Mock(), Mock())
    interface.hit_grid[0][0] = 'H'
    interface.hit_grid[1][1] = 'M'
    assert interface.check_shot_valid(0, 0, Mock()) == False
    assert interface.check_shot_valid(1, 1, Mock()) == False
    assert interface.check_shot_valid(2, 2, Mock()) == True

def test_shot_miss():
    game = Game()
    ui = UserInterface(Mock(), game)
    ui.check_shot_hit(0, 0)
    assert ui.hit_grid[0][0] == 'M'
    assert game.lives == 17

def test_shot_hit():
    game = Game()
    ui = UserInterface(Mock(), game)
    game.place_ship(length= 3, orientation="horizontal", row=5, col=4)
    ui.check_shot_hit(5, 5)
    assert ui.hit_grid[5][5] == 'H'

def test_shot_hit_decrement_lives():
    game = Game()
    ui = UserInterface(Mock(), game)
    game.place_ship(length= 3, orientation="horizontal", row=5, col=4)
    ui.check_shot_hit(5, 5)
    assert game.lives == 16