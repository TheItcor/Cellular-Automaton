import random
import time
import os
from language import *

seed = random.randint(1, 999999999999999999)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        clear()  
        
        for row in self.grid:
            print(''.join('#' if cell else ' ' for cell in row))
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


def check_language():
    try:
        with open("data.txt", 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            
            if not first_line:
                return 'en'
                
            language = first_line[:2].lower()
                
            return language
            
    except FileNotFoundError:
        return 'en'


language = check_language()
tr = lambda key: translate(language, key)


if __name__ == "__main__":
    version = "      Cellular Automaton BETA v 1.3     "
    height = 30
    width = 30
    times = 100



    ## Menu
    menu = True
    run = True
    while run:
        while menu:
            language = check_language()
            clear()

            line()
            print(version)
            print("      \u001b[1mAuthor: Itcor (Aleksandr Shewchuk)\u001b[0m")
            line()
            print("Commands:")
            print(f"-lang  - ", tr("change_lang"))
            print("-setbox", tr('wid_hei_bx') , f"[{width}/{height}]")
            print("-setgen", tr('num_of_gen'), f"[{times}]")
            print("-setseed", tr('seed'))
            print("-start", tr('start'))
            line()
            print(tr("enter_button"))

            command = input("> ").split()
            match (command[0]):
                case "-lang":
                    ## Choice of language
                    clear()
                    line()
                    print(tr("choice_lang"))
                    print(all_language)
                    print(tr("example_lang"))
                    line()

                    language_choice = input()

                    with open('data.txt', 'r') as f:
                        lines = f.readlines()

                    new_lines = [f"{language_choice}\n"] + lines[1:]

                    with open('data.txt', 'w') as f:
                        f.writelines(new_lines)

                case "-setbox":
                    ## Settings for box
                    height = int(command[1])
                    width = int(command[2])

                case "-setgen":
                    ## Settings for generations
                    times = int(command[1])    

                case "-setseed":
                    ## Seed for generatins
                    seed = int(command[1])
                    random.seed(seed)

                case "-start":
                    ## Start
                    menu = False

        
        ## Starting 
        automaton = CellAutomaton(height, width)
        automaton.initialize_randomly()
            
        for generation in range(1, times+1):
            automaton.print_grid()
            automaton.next_generation()
            print(tr('gen'), f"{generation}")
            print(f"Seed: {seed}")
            time.sleep(0.5)

        print(tr('end'))
        input(tr('enter'))    
        menu = 1