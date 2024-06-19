from tkinter import * 
import random 

#constant 
GAME_WIDTH = 700 
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50 
BODY_PARTS = 3
SNAKE_COLOR = '#00ff00'
FOOD_COLOR = '#ff0000'
BG_COLOR = '#000000'

class Snake: 
  def __init__(self): 
    
    self.body_size = BODY_PARTS 
    self.coordinates = [] 
    self.squares = [] 
    for i in range(0, BODY_PARTS): 
      self.coordinates.append([0,0])
    for x , y in self.coordinates: 
      squre = canvas.create_rectangle(x , y , x + SPACE_SIZE , y + SPACE_SIZE , fill = SNAKE_COLOR , tag = 'snake')
      self.squares.append(squre)

class Food: 

  def __init__(self):
    x = random.randint(0,(GAME_WIDTH/SPACE_SIZE-1)) * SPACE_SIZE
    y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE-1)) * SPACE_SIZE  
    self.coordinates = [x,y] 
    canvas.create_oval(x , y , x + SPACE_SIZE , y + SPACE_SIZE ,fill = FOOD_COLOR , tag ='food' ) 

def next_turn(sanke, food):
  x , y = sanke.coordinates[0] 
  if direction == 'up':
    y -= SPACE_SIZE
  elif direction == 'down':
    y += SPACE_SIZE 
  elif direction == 'left':
    x -= SPACE_SIZE 
  elif direction == 'right': 
    x += SPACE_SIZE 
  sanke.coordinates.insert(0, (x,y))
  squre = canvas.create_rectangle(x , y , x + SPACE_SIZE, y+ SPACE_SIZE, fill=SNAKE_COLOR)
  snake.squares.insert(0,squre)
  if x == food.coordinates[0] and y == food.coordinates[1]:
    global score 
    score += 1 
    Label.config(text='score:{}'.format(score))
    canvas.delete('food')
    food = Food()

  else:
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1]) 
    del snake.squares[-1]

  if check_collisions(snake):
    game_over()
  else:
    windwo.after(SPEED,next_turn,snake,food)

def change_direction(new_direction): 

  global direction 

  if new_direction == 'left': 
    if direction != 'right':
      direction = new_direction

  elif new_direction == 'right': 
    if direction != 'left':
      direction = new_direction 
      
  elif new_direction == 'up': 
    if direction != 'down':
      direction = new_direction   

  elif new_direction == 'down': 
    if direction != 'up':
      direction = new_direction

def check_collisions(snake):
  x , y = snake.coordinates[0]

  if x < 0 or x >= GAME_WIDTH:
    return True 
  
  elif y < 0 or y >= GAME_HEIGHT: 
    return True

  for body_part in snake.coordinates[1:]: 
    if x == body_part[0] and y == body_part[1]: 
      return True 
    
  return False


def game_over(): 
  canvas.delete(ALL) 
  canvas.create_text(canvas.winfo_width()/2 , canvas.winfo_height()/2, font = ('consolas',70),text = 'GAME OVER', fill='red',tag='game over')

windwo = Tk() 
windwo.title('Snake Game')
windwo.resizable(False , False)

score  = 0 
direction = 'down' 

Label = Label(windwo,text ='Score:{}'.format(score),font=('consolas',40))
Label.pack()

canvas = Canvas(windwo, bg = BG_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

windwo.update()
window_width = windwo.winfo_width() 
window_height = windwo.winfo_height() 
screen_width = windwo.winfo_screenwidth()
screen_height = windwo.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2)) 

windwo.geometry(f'{window_width}x{window_height}+{x}+{y}')

windwo.bind('<Left>', lambda event: change_direction('left'))
windwo.bind('<Right>', lambda event: change_direction('right'))
windwo.bind('<Up>', lambda event: change_direction('up'))
windwo.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)

windwo.mainloop()

