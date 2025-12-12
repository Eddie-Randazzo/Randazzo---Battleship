from battleship_players import HumanPlayer, AIPlayer
from battleship_classes import HIT, MISS, BOARD_SIZE

def setup_game():
    "Initializes player objects and performs ship placement."
    player = HumanPlayer("Player 1")
    ai = AIPlayer()
    
    player.manual_place_ships()
    ai.random_place_ships()
    
    print("\n" + "="*40 + "\nShips Placed. Game Start!\n" + "="*40)
    return player, ai
    
def update_boards_and_check_win(attacker, defender, target_row, target_col):
    "Fires a shot, updates boards, and checks for win condition."
    # 1. Defender receives the shot
    result, sunk_ship = defender.ship_board.receive_shot(target_row, target_col)
    
    # 2. Attacker updates their tracking board
    if result in (HIT, MISS):
        attacker.tracking_board.grid[target_row][target_col] = result
        print(f"Shot at ({target_row},{target_col}): **{ 'HIT' if result == HIT else 'MISS'}**")
        
        if sunk_ship:
            print(f"\n*** You sunk the opponent's {sunk_ship.name}! ***")
        
    elif result == 'DUPLICATE':
        print("Shot rejected (duplicate target).") # Should only happen with fault AI/input logic
        
    # 3. Check for win
    # FIX 3: Corrected defender.ship_baord to defender.ship_board
    if defender.ship_board.all_ships_sunk():
        # FIX 4: Corrected ]n to \n
        print(f"\n!!! GAME OVER: {attacker.name} WINS !!!")
        print("\nFinal Opponent Board:")
        defender.ship_board.display_board(show_ships=True)
        return True
    
    return False

def game_loop(player, ai):
    # The main turn-based loop."
    current_turn = 0
    game_over = False
    
    while not game_over:
        current_turn += 1
        print(f"\n--- Turn {current_turn} ---")
        
        # --- Player Turn (Attack AI) ---
        print(f"\n{player.name}'s Turn (Target: {ai.name}): ")
        print("Your Target Board:") # Corrected the missing colon for style
        player.tracking_board.display_board(show_ships=False)
        print("Your Ship Board:")
        player.ship_board.display_board(show_ships=True)
        
        r, c = player.get_shot_target()
        game_over = update_boards_and_check_win(player, ai, r, c)
        if game_over: break
        
        # --- AI Turn (Attack Player) ---
        print(f"\n{ai.name}'s Turn...")
        ai_r, ai_c = ai.get_shot_target()
        print(f"{ai.name} targets ({ai_r},{ai_c}).")
        
        game_over = update_boards_and_check_win(ai, player, ai_r, ai_c)
        
        # Display player's ship board after AI shot to show damage
        if not game_over:
            print("\nYour Ship Board (Updated after AI shot):")
            # FIX 5: Corrected player.ship_baord to player.ship_board
            player.ship_board.display_board(show_ships=True)
            input("\nPress Enter to continue to the next turn...")

def main():
    "Entry point of the program."
    print("Welcome to Command Line Battleship!")
    try:
        player,ai = setup_game()
        game_loop(player, ai)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Exiting game.")
        
if __name__ == "__main__":
    main()