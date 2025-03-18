# The Cellular Automaton (Life Simulator)
### 34 languages supported!

![изображение](https://github.com/user-attachments/assets/e0401332-50fb-49e2-bbd8-ebfa91c2e549)


## Usage
fast start:
Run main.py
Input `-start`

| Commands  | explanation |
| ------------- | ------------- |
| `-lang` | change language |
| `-setb [width] [height]`  | change the size for the window where the cellular automaton will be.  |
| `-setg [number]`  | change the number of generations  |
| `-start`  | for start simulation!  |

Also you can change language: 
`-lang` ---> `en`, `es`, `fr`, etc...

## Features
![изображение](https://github.com/user-attachments/assets/f07ac85a-b509-40d5-8c1e-cd29df66a97b)
- Change generation map size
- Change number of generations
- Сhange language (supported 34 languages)
- Start random simulation

## Project structure
Cellular Automaton/  
  ├── src/  
  │   ├── main.py      - class Cell Automaton, menu interface  
  │   └── language.py  - all translations  
  ├── data.txt         - user data (For now, only for storing the language the user uses)  
  └── README.md  
