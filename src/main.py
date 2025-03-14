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

def check_language():
    try:
        with open("data.txt", 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            
            if not first_line:
                print("Файл пустой. Используем язык по умолчанию 'en'")
                return 'en'
                
            language = first_line[:2].lower()
            
            # Проверка на допустимые коды языков (опционально)
            valid_languages = ['en', 'ru', 'es']
            if language not in valid_languages:
                print(f"Неизвестный код языка '{language}'. Используем 'en'")
                return 'en'
                
            return language
            
    except FileNotFoundError:
        print(f"Файл не найден. Используем язык по умолчанию 'en'")
        return 'en'



if __name__ == "__main__":
    language = check_language()
    version = "BETA v 1.0"
    height = 50
    width = 40
    times = 101



    ## Menu
    menu = True
    run = True
    while run:
        while menu:
            os.system('cls' if os.name == 'nt' else 'clear')

            line()
            print("      Cellular Automaton BETA v 1.0     ")
            print("      \u001b[1mAuthor: Itcor (Aleksandr Shewchuk)\u001b[0m")
            line()
            print("Commands:")
            print("-lang [en/ru/es]  -  Change language")
            print(f"-setb [width] [height] - Change box size [{width}/{height}]")
            print(f"-setg [number] - How manu generatings be [{times}]")
            print("-start")
            line()
            print("Enter your command:")

            command = input("> ").split()
            match (command[0]):
                case "-lang":
                    print("Changes!")

                case "-setb":
                    height = int(command[1])
                    width = int(command[2])

                case "-setg":
                    times = int(command[1])    

                case "-start":
                    menu = False

        
        ## Starting 
        automaton = CellAutomaton(height, width)
        automaton.initialize_randomly()
            
        for generation in range(1, times):
            print(f"Generation: {generation}")
            automaton.print_grid()
            automaton.next_generation()
            time.sleep(0.2)

        print("End of generations")
        input("Enter for continue")    
        menu = 1