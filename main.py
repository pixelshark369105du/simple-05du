"""Simple 2‑D grid game prototype.  
Move with 'w', 'a', 's', 'd'; quit with 'q'."""

import sys

WIDTH, HEIGHT = 10, 5
player = [HEIGHT // 2, WIDTH // 2]

while True:
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    grid[player[0]][player[1]] = '@'
    print('\n'.join(''.join(row) for row in grid))
    cmd = input("Move (w/a/s/d) or q to quit: ").strip().lower()
    if cmd == 'q':
        break
    if cmd == 'w' and player[0] > 0:
        player[0] -= 1
    elif cmd == 's' and player[0] < HEIGHT - 1:
        player[0] += 1
    elif cmd == 'a' and player[1] > 0:
        player[1] -= 1
    elif cmd == 'd' and player[1] < WIDTH - 1:
        player[1] += 1
    else:
        print("Invalid move.")