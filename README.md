# 🧩 Peg Solitaire in Python

A console-based Peg Solitaire game implemented in Python, created for educational purposes. The code demonstrates fundamental concepts like list manipulation, condition checking, user input handling, and game state management.

---

## 📌 Author

**Nikolaos Laloutsos**  

---

## 🎯 Project Goal

The goal of this project is to:
- Understand and interact with a classic **Peg Solitaire** board game.
- Learn core Python programming concepts through game logic.
- Practice working with 2D lists, functions, loops, and conditionals.

---

## 🕹️ Game Description

Peg Solitaire is a logic puzzle game involving movement of pegs on a board. The objective is to eliminate pegs by jumping over them until only one remains.

### 🔧 Game Features
- Console-based board rendering.
- Input system to allow user to make moves (`L`, `R`, `U`, `D`).
- Score system to show remaining pegs.
- Game-over detection when no valid moves remain.
- Robust input validation.

---

## 🗂️ File Structure

- `board`: A 2D list representing the game board.
- `voc1`, `voc2`: Dictionaries used for converting input coordinates.
- `printboard()`: Displays the current state of the board.
- `move()`: Handles logic for valid moves in all directions.
- `invalid_input()`: Validates user input format.
- `finish_game()`: Checks if any moves are left.
- `score()`: Displays final score (remaining pegs).
- `move_again()`: Main input loop to keep the game running.

---

## ▶️ How to Play

1. Run the script in a Python environment.
2. Follow the prompt:  
   Enter a peg's position followed by a direction.  
   **Example input:** `C4L` → Move the peg at C4 to the left.
3. Valid directions:
   - `L`: Left
   - `R`: Right
   - `U`: Up
   - `D`: Down
4. The game ends when no valid moves remain.

---

## 🚫 Invalid Moves

- If the selected peg doesn't exist.
- If the direction leads out of bounds.
- If there's no peg to jump over.
- If the landing spot is already occupied.

---

## 🧠 Educational Value

This project is ideal for:
- Beginners learning Python.
- Students interested in logic-based game programming.
- Anyone looking to practice control flow and list management.

---

## 📌 Notes

- Only basic libraries are used (no external dependencies).
- Tested in standard Python 3.x environments.
- Code comments are minimal — you’re encouraged to read and trace the code manually for learning purposes!

---

## 📜 License

This project is for academic and learning purposes only.  
Feel free to fork and build upon it.
