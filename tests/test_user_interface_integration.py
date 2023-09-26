import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
