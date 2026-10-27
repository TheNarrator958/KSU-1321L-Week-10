# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : Assignment 5B

import random

def generate_map(rows, cols):
    game_map = []
    treasures = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            num = random.randint(0, 100)
            if num < 30:
                row.append("T")
                treasures += 1
            elif num < 50:
                row.append("X")
            else:
                row.append("E")
        game_map.append(row)
    return game_map, treasures

def display_map(game_map):
    for r in range(len(game_map)):
        line = ""
        for c in range(len(game_map[r])):
            line += game_map[r][c] + " "
        print(line.strip())

def explore(game_map, location, score, remaining, streak, traps, explored):
    """Process one exploration; returns the updated game state."""
    row, col = location
    cell = game_map[row][col]

    if cell == "T":
        remaining -= 1
        streak += 1
        explored += 1
        if streak >= 2:
            score += 15
            print("Treasure found! +15 points (including bonus).")
        else:
            score += 10
            print("Treasure found! +10 points.")
        game_map[row][col] = "V"
    elif cell == "X":
        score -= 5
        streak = 0
        traps += 1
        explored += 1
        print("You hit a trap! -5 points.")
        game_map[row][col] = "V"
    elif cell == "E":
        streak = 0
        explored += 1
        print("Nothing found at this location.")
        game_map[row][col] = "V"
    else:
        # Already visited: no change, and the streak is NOT reset
        print("You have already explored this location.")

    return score, remaining, streak, traps, explored

def main():
    rows = int(input("Enter rows : "))
    cols = int(input("Enter Columns : "))

    game_map, remaining = generate_map(rows, cols)
    print("Total Treasures :", remaining)
    display_map(game_map)

    score = 0
    streak = 0
    traps = 0
    explored = 0

    while remaining > 0:
        row = int(input("Enter row (0 to " + str(rows - 1) + ") : "))
        col = int(input("Enter column (0 to " + str(cols - 1) + ") : "))
        location = (row, col)

        score, remaining, streak, traps, explored = explore(
            game_map, location, score, remaining, streak, traps, explored
        )

        display_map(game_map)
        print("Current score =", score)
        print("Remaining Treasures =", remaining)

    print("Congratulations! All treasures have been collected!")
    print("Final Map:")
    display_map(game_map)
    print("Final Score =", score)
    print("Traps Encountered =", traps)
    print("Locations explored =", explored)

main()