import random
from battleship_classes import Board, Ship, SHIP_TYPES, BOARD_SIZE, WATER, HIT, MISS

class HumanPlayer:
    def __init__(self, name="Human"):
        self.name = name
        self.ship_board = Board()
        self.tracking_board = Board() # Tracks shots on opponent's board
        
    def manual_place_ships(self):
        """Handles manual input and validation for ship placement."""
        print(f"\n--- {self.name}'s Ship Placement ---")
        
        # 🌟 ADDED LINE: Display the empty board before starting placement
        print("Empty Board:")
        self.ship_board.display_board(show_ships=True)
        
        for name, length in SHIP_TYPES.items():
            ship = Ship(name, length)
            placed = False
            while not placed:
                print(f"Placing {name} (Length: {length}).")
                
                try:
                    coords = input("Enter starting coordinates (row,col): ").replace(" ", "").split(',')
                    start_row, start_col = int(coords[0]), int(coords[1])
                    orientation = input("Enter orientation (H/V): ").upper()
                except (ValueError, IndexError):
                    print("Invalid input format. Try again (e.g., 3, 4 and H).")
                    continue
                
                if self.ship_board.is_valid_placement(length, start_row, start_col, orientation):
                    self.ship_board.place_ship(ship, start_row, start_col, orientation)
                    # Display the board after successful placement
                    print(f"\n{name} Placed. Current Board Status:")
                    self.ship_board.display_board(show_ships=True) 
                    placed = True
                else:
                    print("Invalid placement. Ship is out of bounds, overlaps, or orientation is wrong. Try again.")
                    
    def get_shot_target(self):
        # "Gets target coordinates from the user with validation."
        while True:
            try:
                target = input("Enter target coordinates (row,col): ").replace(" ", "").split(',')
                row, col = int(target[0]), int(target[1])
            except (ValueError, IndexError):
                print("Invalid input format. Enter two numbers separated by a comma (e.g., 5,8).")
                continue
            
            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                print("Coordinates out of bounds (0-9). Try again.")
            # Check tracking board to prevent duplicate shots
            elif self.tracking_board.grid[row][col] != WATER:
                print("You have already shot at that location. Try a new target.")
            else:
                return row, col
            
class AIPlayer:
    def __init__(self, name="AI"):
        self.name = name
        self.ship_board = Board()
        self.tracking_board = Board()
        
        # 🌟 CRITICAL FIX: Changed 'self.untried_target' to 'self.untried_targets'
        self.untried_targets = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)]
        random.shuffle(self.untried_targets)
        
    def random_place_ships(self):
        # "Randomly places all ships."
        for name, length in SHIP_TYPES.items():
            ship = Ship(name, length)
            placed = False
            while not placed:
                start_row = random.randint(0, BOARD_SIZE - 1)
                start_col = random.randint(0, BOARD_SIZE - 1)
                orientation = random.choice(['H', 'V'])
                
                if self.ship_board.is_valid_placement(length, start_row, start_col, orientation):
                    self.ship_board.place_ship(ship, start_row, start_col, orientation)
                    placed = True
                    
    def get_shot_target(self):
        # "Basic AI: Selects a random untried coordinate."
        # Pop the last element for a random shot
        if self.untried_targets:
            row, col = self.untried_targets.pop()
            return row, col
        return -1, -1 # Error state (should not happen in a standard game)