import os
from getkey import getkey, keys
import sys

sys.setrecursionlimit(10000000)
name = input("Name: ")

dna = 0
dps = 0
dpc = 1
orgCount = 0
location = True

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

class Organelle:
  def __init__(self, name, cost, dpc, dps):
    self.name = name
    self.cost = cost
    self.dpc = dpc #DNA per click
    self.dps = dps #DNA per second

  def update_cost(self):
    self.cost += int(self.cost/10)

Flagellum = Organelle("Flagellum", 10, 1, 0)
Cilia = Organelle("Cilia", 15, 2, 0)
Cell_Membrane = Organelle("Cell Membrane", 20, 4, 0)

def shop():
  clear()
  print("test")
  key = getkey()
  if key == "g":
    game()
  
def game():
  global dna, dpc, dps, orgCount
  clear()
  print(f'''
┌───────┐
│💻 MENU│🛒 SHOP         TAB
────────────────────────────
 DNA clicker
────────────────────────────
  🧍 Name: {name} 
  
  🧬 DNA: {dna}
────────────────────────────
 Stats
────────────────────────────
  🧬 DNA/click: {dpc}

  🧬 DNA/second: {dps}

  🦠 Organelles: {orgCount}
  ''')
  key = getkey()

  if key == " ":
    dna += dpc
    game()
  elif key == "\t":
    shop()
  else:
      game()

def shop():
  global orgCount
  clear()
  shop = f'''
        ┌───────┐
 💻 MENU│🛒 SHOP│        TAB
────────────────────────────
[1] Flagellum - {"🧬 "+str(Flagellum.cost)}
────────────────────────────
  +{Flagellum.dpc} DNA/click

    A flagellum is a hair-like
  organelle that gives some
  animal and plant cells the
  ability to move.
────────────────────────────
[2] Cilia - {"🧬 "+str(Cilia.cost)}
────────────────────────────
  +{Cilia.dpc} DNA/click
  
    A cilium is a hair-like
  organelle
  '''
  print(shop)

  key = getkey()
  if key == "\t":
    game()
  elif key == "1":
    orgCount += 1
    shop()

game()