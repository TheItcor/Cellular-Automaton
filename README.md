# The Cellular Automaton (Life Simulator)
### 56 languages supported!

![изображение](https://github.com/user-attachments/assets/e0401332-50fb-49e2-bbd8-ebfa91c2e549)


## Usage
fast start:
Run main.py
Input `-start`

| Commands  | explanation |
| ------------- | ------------- |
| `-lang` | change language |
| `-setbox [width] [height]`  | change the size for the window where the cellular automaton will be  |
| `-setgen [number]`  | change the number of generations  |
| `-setseed`  | change random seed  |
| `-start`  | for start simulation!  |

Also you can change language: 
`-lang` ---> `en`, `es`, `fr`, etc...

## Features
![изображение](https://github.com/user-attachments/assets/f07ac85a-b509-40d5-8c1e-cd29df66a97b)
- Change generation map size
- Change generation seed
- Change number of generations
- Сhange language (supported 56 languages)
- Start random simulation

## Project structure
Cellular Automaton/  
  ├── src/  
  │   ├── main.py      - class Cell Automaton, menu interface  
  │   └── language.py  - all translations  
  ├── data.txt         - user data (For now, only for storing the language the user uses)  
  └── README.md  
