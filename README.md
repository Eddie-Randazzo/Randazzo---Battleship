# 🚢 Battleship Game (CLI)

**Project Title:** Command Line Battleship

**Author:** Eddie Randazzo

## 🎯 Objective
This project implements the classic two-player Battleship game in a Python Command Line Interface (CLI). The game supports a single-player mode against a basic AI opponent.

## 🛠️ Technology Stack
* **Language:** Python
* **Interface:** Command Line Interface (CLI)

## 🚀 How to Run the Game

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Eddie-Randazzo/Randazzo---Battleship
    cd Randazzo---Battleship
    ```
2.  **Navigate to the source directory:**
    ```bash
    cd src
    ```
3.  **Execute the main file:**
    ```bash
    python main_game.py
    ```

## 🎮 Game Rules & Instructions
The game uses a standard 10x10 board (coordinates 0-9).

### Ship Placement
The player must manually place 5 ships. The game will prompt for:
1.  Starting coordinate (e.g., `3,4`)
2.  Orientation (`H` for Horizontal or `V` for Vertical)

### Gameplay
* Players alternate turns firing shots at the opponent's board.
* Input is validated to ensure coordinates are on the board and have not been targeted previously.
* **Win Condition:** The first player to sink all 5 of the opponent's ships wins the game.

## 📂 Source File Structure (src/)
| File | Description |
| :--- | :--- |
| `main_game.py` | Main execution file. Handles game setup, the turn loop, and win/loss conditions. |
| `battleship_players.py` | Contains the `HumanPlayer` and `AIPlayer` classes and their specific logic (input, randomized targeting). |
| `battleship_classes.py` | Defines the core game objects: `Ship` and `Board` (handling grid operations, placement, and hit detection). |
