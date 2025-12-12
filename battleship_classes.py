import random

# Constants
BOARD_SIZE = 10
SHIP_TYPES = {
    "Carrier": 5,
    "Battleship": 4,
    "Destroyer": 3,
    "Submarine": 3,
    "Patrol Boat": 2
}

# Display Symbols
WATER = '~'
SHIP = 'S'
MISS = 'O'
HIT = 'X'

class Ship:
    "Represents a ship with its status."
    # FIX 1: Corrected constructor name from _init__ to __init__
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.coordinates = []  # List of tuples (row, col)
        self.hits = 0
        
    def is_sunk(self):
        "Checks if the ship has taken damage equal to its length."
        return self.hits >= self.length
    
    def register_hit(self):
        "Increments the hit count."
        self.hits += 1
        
class Board:
    "Manages the 10x10 game board, ships, and shot detection."
    def __init__(self, size=BOARD_SIZE):
        #grid: Stores the actual positions of ships ('S', 'X', '~', 'O')
        self.grid = [[WATER for _ in range(size)] for _ in range(size)]
        self.ships = [] # List of Ship objects
        
    def display_board(self, show_ships=True):
            "Prints the board to the CLI."
            header = "   " + " ".join(str(i) for i in range(BOARD_SIZE))
            print(header)
            for i in range(BOARD_SIZE):
                row_display = []
                for j in range(BOARD_SIZE):
                    cell = self.grid[i][j]
                    if cell == SHIP and not show_ships:
                        row_display.append(WATER)
                    else:
                        row_display.append(cell)
                print(f"{i:<2} {' '.join(row_display)}")
                
    def is_valid_placement(self, length, start_row, start_col, orientation):
        "Validates if a ship can be placed at the given location."
        coords = []
        if orientation == 'H':
            if start_col + length > BOARD_SIZE:
                return False
            coords = [(start_row, start_col + i) for i in range(length)]
        elif orientation == 'V':
            if start_row + length > BOARD_SIZE:
                return False
            coords = [(start_row + i, start_col) for i in range(length)]
        else:
            return False
            
        # Check for overlap and bounds
        for r, c in coords:
            if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
                return False
            if self.grid[r][c] != WATER:
                return False
        return True
        
    def place_ship(self, ship, start_row, start_col, orientation):
        "Places a ship on the grid"
        coords = []
        for i in range(ship.length):
            r = start_row + (i if orientation == 'V' else 0)
            c = start_col + (i if orientation == 'H' else 0)
            self.grid[r][c] = SHIP
            coords.append((r, c))
            
        # These lines MUST be outside the 'for' loop to add the ship only once.
        ship.coordinates = coords
        self.ships.append(ship)
    
    def receive_shot(self, row, col):
        "Processes an incoming shot, returns the result and the sunk ship (if any)."
        target = self.grid[row][col]
        sunk_ship = None
        result = 'DUPLICATE' # Default result for hitting an already hit/missed spot

        if target == SHIP:
            # 1. Update the grid visually
            self.grid[row][col] = HIT 
            result = HIT
            
            # 2. Find and update the ship object
            for ship in self.ships:
                if (row, col) in ship.coordinates:
                    ship.register_hit()
                    if ship.is_sunk():
                        sunk_ship = ship
                    break # Stop searching once the ship is found
                    
        elif target == WATER:
            self.grid[row][col] = MISS
            result = MISS
            
        return result, sunk_ship
            
    def all_ships_sunk(self):
        "Checks if every ship on the board is sunk."
        return all(ship.is_sunk() for ship in self.ships)