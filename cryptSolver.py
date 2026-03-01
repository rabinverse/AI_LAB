# This program solves a cryptarithm (alphametic) puzzle using brute force.


from itertools import permutations

# Letters in the puzzle
letters = "BASELGM"

# All possible digit assignments
for perm in permutations(range(10), len(letters)):
    B, A, S, E, L, G, M = perm

    # Leading letters cannot be zero
    if B == 0 or G == 0:
        continue

    # Form the numbers
    BASE = B * 1000 + A * 100 + S * 10 + E
    BALL = B * 1000 + A * 100 + L * 10 + L
    GAMES = G * 10000 + A * 1000 + M * 100 + E * 10 + S

    # Check if the sum holds
    if BASE + BALL == GAMES:
        print(f"BASE = {BASE}, BALL = {BALL}, GAMES = {GAMES}")
        # break


#   BASE
# + BALL
# ------
#  GAMES
