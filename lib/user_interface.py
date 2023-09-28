from lib.ship import Ship

class UserInterface:
    def __init__(self, io, game, name=''):
        self.io = io
        self.game = game
        self.unplaced_ships = self.game.starting_ships()
        self.name = name
        self.hit_grid = [['.' for i in range(10)] for i in range(10)]

    def run(self):
        self._show(f"Welcome to the game, {self.name}!")
        self._show("Set up your ships first.")
        while len(self.unplaced_ships) > 0:
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message()))
            self._show("This is your board now:")
            self._show(self._format_board())
            self._prompt_for_ship_placement()

    def ship_overlap(self, row, col, length=1, orientation='h'):
        if orientation == 'h':
            for i in range(length):
                for ship in self.game.ships_placed:
                    if ship.covers(row, col+i):
                        return True
        else:
            for i in range(length):
                for ship in self.game.ships_placed:
                    if ship.covers(row+i, col):
                        return True
        return False
    
    def start_ship_placement(self, length, orientation, row, col):
        success = self.game.place_ship(
            length, 
            {"v": "vertical", "h": "horizontal"}[orientation], 
            row, 
            col
        )
        if success:
            self.unplaced_ships.remove(Ship(length))
        
    def check_shot_hit(self, row, col):
        '''
        check if a ship covers the coordinate
        update hit_grid with hit or miss
        decrement lives counter if hit
        '''
        if self.ship_overlap(row, col):
            self.hit_grid[row][col] = "H"
            self.game.lives -= 1
        else:
            self.hit_grid[row][col] = "M"

    def check_shot_valid(self, row, col):
        if col not in range(1,11) or row not in range(1,11):
            if row == -2 and col == -2:
                print("That shot is out of bounds. Please try again.")
            return False
        elif self.hit_grid[row][col] != ".":
            print("You've already shot there. Please try again.")
            return False
        else:
            return True

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.unplaced_ships]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self):
        ship_length = int(self._prompt("Which do you wish to place?"))
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = int(self._prompt("Which row?"))
        ship_col = int(self._prompt("Which column?"))
        if not self.ship_overlap(ship_row, ship_col, ship_length, ship_orientation):
            self.start_ship_placement(ship_length, ship_orientation, ship_row, ship_col)
        else:
            print("You already have a ship placed there!")
    
    def _prompt_for_shot(self, opp_ui):
        self._show(f"It's {self.name}'s turn to shoot!")
        self._show(opp_ui._format_hit_grid())
        shot_row = -1
        shot_col = -1
        while not self.check_shot_valid(shot_row - 1, shot_col -1):
            shot_row = int(self._prompt("Which row?"))
            shot_col = int(self._prompt("Which column?"))

        if self.check_shot_valid(shot_row - 1, shot_col -1):
            opp_ui.check_shot_hit(shot_row - 1, shot_col - 1)

    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("  ".join(row_cells))
        return "\n".join(rows)

    def _format_hit_grid(self):
        hit_grid_string = ""
        for row in self.hit_grid:
            hit_grid_string += "  ".join(row) + "\n"
        return hit_grid_string
        
