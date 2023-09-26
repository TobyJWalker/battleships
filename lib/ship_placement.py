class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        if col not in range(1,11) or row not in range(1,11):
            self.valid = False
        else:
            if row + length > 10 and orientation == "horizontal":
                self.valid = False
            elif col + length > 10 and orientation == "vertical":
                self.valid = False
            else:
                self.row = row
                self.col = col
                self.valid = True       

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
