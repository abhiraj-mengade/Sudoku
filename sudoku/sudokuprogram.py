from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import random
from random import sample
import math
import copy

n=4
print("Welcome to SUDOKU player! ")
level = input("Choose a difficulty level: a)easy b)hard. Type a or b.\n ").lower()
if level == "a" :
  n=4
elif level == "b" :
  n = 9

def solved(base):
  side  = base*base
  def pattern(r,c): return (base*(r%base)+r//base+c)%side
  def shuffle(s): return sample(s,len(s)) 
  rBase = range(base) 
  rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
  cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
  nums  = shuffle(range(1,base*base+1))
  board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
  return board


def unsolved(grid):
  sample = grid
  for i in range((n**2)*3//4):
    sample[random.randint(0,n-1)][random.randint(0,n-1)]=" "
  return sample


def print_grid(board):
  def expandLine(line):
    base = int(math.sqrt(n))
    return line[0] + line[5:9].join([line[1:5] * (base - 1)] * base) + line[9:13]


  line0 = expandLine("╔═══╤═══╦═══╗")
  line1 = expandLine("║ . │ . ║ . ║")
  line2 = expandLine("╟───┼───╫───╢")
  line3 = expandLine("╠═══╪═══╬═══╣")
  line4 = expandLine("╚═══╧═══╩═══╝")

  side = n
  print(line0)
  for r in range(1, side + 1):
      print("".join(  f"{s}" + f"{num}" for s,num  in zip(line1.split("."), board[r - 1])))
      print([line2, line3, line4][(r % side == 0) + (r % n == 0)])
      
def pdf_grid():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("index.html")
    template_vars = {"M" : unsolved_board, "N" : solved_board}
    html_out = template.render(template_vars)
    HTML(string=html_out, base_url='.').write_pdf("sudokupuzzle.pdf",stylesheets=["style.css"])
    
solved_board = solved(int(math.sqrt(n)))
solved_board_copy=copy.deepcopy(solved_board)
unsolved_board = unsolved(solved_board_copy)     


answer = input("Do you want a printable copy of the puzzle? Enter yes or no:") 
if answer == "yes": 
    pdf_grid() 
elif answer == "no":
    print("\nOkay!")  
else:
    print("Please enter yes or no.\n") 

print("There you go!..\n")
print_grid(unsolved_board)

answer = input("\nDo you wish to see the solution? Enter yes or no:\n") 
if answer == "yes": 
    print_grid(solved_board)
    print("\n Hope you had fun!:)")
elif answer == "no":
    print("\nOkay! Have fun solving.")
else:
    print("\nPlease enter yes or no.") 


