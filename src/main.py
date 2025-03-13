import random
import time
import os

class CellAutomaton:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
    

    def initialize_randomly(self, alive_prob=0.3):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = 1 if random.random() < alive_prob else 0
    

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        ## Clear screen
        for row in self.grid:
            print(' '.join('▓' if cell else '░' for cell in row))
        print()
    

    def count_neighbors(self, row, col):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < self.height and 0 <= new_col < self.width:
                    count += self.grid[new_row][new_col]
        return count
    

    def next_generation(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j]:
                    new_grid[i][j] = 1 if neighbors in (2, 3) else 0
                else:
                    new_grid[i][j] = 1 if neighbors == 3 else 0
        self.grid = new_grid


def line():
    print("\u001b[33m" + "===============================================" + "\u001b[0m")



if __name__ == "__main__":
    ## Menu
    line()
    print("      Life Simulator aka Cellular Automaton")
    print("")
    line()


    input()





    automaton = CellAutomaton(40, 20)
    automaton.initialize_randomly()
    
    for generation in range(1, 101):
        print(f"Generation: {generation}")
        automaton.print_grid()
        automaton.next_generation()
        time.sleep(0.2)


