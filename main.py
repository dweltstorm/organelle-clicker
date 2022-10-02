import os
import time
from getkey import getkey
import sys
import timeit

sys.setrecursionlimit(2147483647)
name = input("Name: ")

dna = 0
dps = 0
dpc = 1
orgCount = 0
inventory = []

def rgb(r,g,b):
  return f"\033[38;2;{r};{g};{b}m"

reset = "\033[0m"
red = rgb(255,0,0)
green = rgb(0,255,0)
light_blue = rgb(82,180,255)
light_brown = rgb(190,140,100)
brown = rgb(170,120,80)
golden = rgb(219,180,107)

def clear():
  os.system('cls' if os.name=='nt' else 'clear')

class Organelle:
  def __init__(self, name, cost, dpc, dps):
    self.name = name
    self.cost = cost
    self.dpc = dpc #DNA per click
    self.dps = dps #DNA per second

def update_cost(self):
  self.cost += int(self.cost/10)

Flagellum = Organelle("Flagellum", 10, 1, 0)
Cilium = Organelle("Cilium", 15, 2, 0)
CellMembrane = Organelle("Cell Membrane", 20, 4, 0)

def processPurchase(organelle):
  global dna, dpc, orgCount, inventory
  if (dna - organelle.cost) < 0:
    print(f"{red}Not enough DNA!{reset}")
    time.sleep(0.5)
    shop()
  else:
    dna -= organelle.cost
    inventory.append(organelle)
    orgCount += 1
    update_cost(organelle)
    dpc += organelle.dpc
    shop()
  
def game():
  global dna, dpc, dps, orgCount
  clear()
  print(f'''
┌───────┐
│💻 MAIN│🛒 SHOP         TAB
────────────────────────────
DNA CLICKER
────────────────────────────
  🧍 Name: {name} 
  
  🧬 DNA: {dna}
────────────────────────────
STATS
────────────────────────────
  🧬 DNA/click: {dpc}

  🧬 DNA/second: {dps}

  🦠 Organelles: {orgCount}
  ''')
  start = timeit.default_timer()
  key = getkey()
  end = timeit.default_timer()

  if key == " " and end - start > 0.1:
    dna += dpc
    game()
  elif key == "\t":
    shop()
  else:
    game()

def shop():
  global orgCount
  global dpc
  global dna
  clear()
  shopScreen = f'''
        ┌───────┐
 💻 MAIN│🛒 SHOP│        TAB
────────────────────────────
[1] Flagellum - {"🧬 "+str(Flagellum.cost)}
────────────────────────────
  +{Flagellum.dpc} DNA/click

    A flagellum is a hair-like
  organelle that gives some
  animal and plant cells the
  ability to move.
────────────────────────────
[2] Cilium - {"🧬 "+str(Cilium.cost)}
────────────────────────────
  +{Cilium.dpc} DNA/click
  
    A cilium is a hair-like
  organelle similar to a
  flagellum, except cilia
  are usually much shorter
  and a cell will have
  hundreds of them.
────────────────────────────
[3] Cell Membrane - {"🧬 "+str(CellMembrane.cost)}
────────────────────────────
  +{CellMembrane.dpc} DNA/click

    The cell membrane is like 
  a wall that protects the
  inside of the cell from 
  its environment.
  '''
  print(shopScreen)
  key = getkey()
  if key == "\t":
    game()
  elif key == "1":
    processPurchase(Flagellum)
  elif key == "2":
    processPurchase(Cilium)
  elif key == "3":
    processPurchase(CellMembrane)
  else:
    shop()
    
game()