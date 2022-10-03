import os
import time
from getkey import getkey
import sys
import timeit
import json


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


def type(x, y):
  for character in x:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(y)


sys.setrecursionlimit(2147483647)

name = input("Name: ")


def check_file():
  x = os.listdir("saves")
  for i in x:
    if f"{name}.json" in i:
      return True
    else:
      return False


if check_file() == True:
  with open(f"saves/{name}.json", "r") as f:
    save = json.load(f)
else:
  save = {"dpc": 1, "dna": 0, "orgCount": 0, "inventory": []}

dpc = int(save["dpc"])
dna = int(save["dna"])
orgCount = int(save["orgCount"])
inventory = save["inventory"]


def rgb(r, g, b):
  return f"\033[38;2;{r};{g};{b}m"


reset = "\033[0m"
red = rgb(255, 0, 0)
green = rgb(0, 255, 0)
light_blue = rgb(82, 180, 255)
light_brown = rgb(190, 140, 100)
brown = rgb(170, 120, 80)
golden = rgb(219, 180, 107)


class Organelle:

  def __init__(self, name, cost, dpc, multiplier):
    self.name = name
    self.cost = cost
    self.dpc = dpc
    self.multiplier = multiplier


def update_cost(self):
  self.cost += int(self.cost / 10)


Flagellum = Organelle("Flagellum", 10, 1, 0)
Cilium = Organelle("Cilium", 50, 2, 0)
CellMembrane = Organelle("Cell Membrane", 100, 4, 0)
CellWall = Organelle("Cell Wall", 150, 6, 0)
Vacuole = Organelle("Vacuole", 300, 8, 0)
Chloroplast = Organelle("Chloroplast", 500, 10, 0)
Ribosome = Organelle("Ribosome", 1000, 15, 0)
Cytoplasm = Organelle("Cytoplasm", 1500, 30, 0)
RoughER = Organelle("Rough ER", 2000, 35, 0)
SmoothER = Organelle("Smooth ER", 10000, 60, 0)
GolgiApparatus = Organelle("Golgi Apparatus", 100000, 100, 0)
Centrosome = Organelle("Centrosome", 200000, 125, 0)
Mitochondria = Organelle("Mitochondria", 300000, 150, 0)
Nucleolus = Organelle("Nucleolus", 500000, 200, 0)
Nucleus = Organelle("Nucleus", 1000000000, 0, 2)


def processPurchase(organelle, operation):
  global dna, dpc, orgCount, inventory
  if (dna - organelle.cost) < 0:
    print(f"{red}Not enough DNA!{reset}")
    time.sleep(0.5)
    shop()
  else:
    dna -= organelle.cost
    inventory.append(str(organelle))
    orgCount += 1
    update_cost(organelle)
    if operation == "add":
      dpc += organelle.dpc
    if operation == "multiply":
      dpc *= organelle.multiplier
    shop()


def drawGame():
  clear()
  print(f'''
┌───────┐
│💻 MAIN│🛒 SHOP                       TAB
───────────────────────────────────────────
DNA CLICKER
───────────────────────────────────────────
  🧍 Name: {name} 
  
  🧬 DNA: {dna}
───────────────────────────────────────────
STATS
───────────────────────────────────────────
  🧬 DNA/click: {dpc}

  🦠 Organelles: {orgCount}
  ''')

def game():
  global dna, dpc, cps, orgCount
  drawGame()
  start = timeit.default_timer()
  key = getkey()
  end = timeit.default_timer()

  if key == " " and end - start > 0.1:
    dna += dpc
    game()
  elif key == "\t":
    shop()
  elif key == "s":
    save()
    print(f"{green}Your game has been saved!{reset}")
    time.sleep(0.5)
    game()
  else:
    game()


def shop():
  global orgCount
  global dpc
  global dna
  clear()
  shopScreen = f'''
        ┌───────┐
 💻 MAIN│🛒 SHOP│                                                                 TAB
──────────────────────────────────────────────────────────────────────────────────────
[1] {Flagellum.name} - {"🧬 "+str(Flagellum.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Flagellum.dpc} DNA/click

    A flagellum is a hair-like organelle that gives some animal and plant cells the 
  ability to move.
──────────────────────────────────────────────────────────────────────────────────────
[2] {Cilium.name} - {"🧬 "+str(Cilium.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Cilium.dpc} DNA/click
  
    A cilium is a hair-like organelle similar to a flagellum, except cilia are usually
  much shorter and a cell will have hundreds of them.
──────────────────────────────────────────────────────────────────────────────────────
[3] {CellMembrane.name} - {"🧬 "+str(CellMembrane.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{CellMembrane.dpc} DNA/click

    The cell membrane is like a wall that protects the inside of the cell from its
  environment. It is also selectively permeable, meaning it allows certain
  substances to pass through.
──────────────────────────────────────────────────────────────────────────────────────
[4] {CellWall.name} - {"🧬 "+str(CellWall.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{CellWall.dpc} DNA/click

    The cell wall is very similar to the cell membrane, except that all types of
  cells have a cell membrane, but only plants and some bacteria and fungi have a cell
  wall.
──────────────────────────────────────────────────────────────────────────────────────
[5] {Vacuole.name} - {"🧬 "+str(Vacuole.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Vacuole.dpc} DNA/click

    The vacuole is a fluid-filled sac that stores stuff like water, food molecules,
  inorganic ions, and enzymes. Plants have what's called a central vacuole, and it's
  the largest organelle in a plant cell.
──────────────────────────────────────────────────────────────────────────────────────
[6] {Chloroplast.name} - {"🧬 "+str(Chloroplast.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Chloroplast.dpc} DNA/click

    Chloroplasts are the organelles that perform photosynthesis. They are highly
  compartmentalized, and have an inner and outer membrane.
──────────────────────────────────────────────────────────────────────────────────────
[7] {Ribosome.name} - {"🧬 "+str(Ribosome.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Ribosome.dpc} DNA/click
  
    Ribosomes are organelles that carry out protein synthesis and are comprised of RNA
  and proteins.
──────────────────────────────────────────────────────────────────────────────────────
[8] {Cytoplasm.name} - {"🧬 "+str(Cytoplasm.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Cytoplasm.dpc} DNA/click

    The cytoplasm is the substance inside of the cell, and it is where organelles are.
──────────────────────────────────────────────────────────────────────────────────────
[9] {RoughER.name} - {"🧬 "+str(RoughER.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{RoughER.dpc} DNA/click

    The rough endoplasmic reticulum is a bunch of thin folded membranes studded with
  ribosomes where proteins and lipids are produced.
──────────────────────────────────────────────────────────────────────────────────────
[0] {SmoothER.name} - {"🧬 "+str(SmoothER.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{SmoothER.dpc} DNA/click

    The smooth endoplasmic reticulum doesn't have ribosomes on its surface. It makes
  lipids and helps break down drugs and alcohol, and doesn't make protie
──────────────────────────────────────────────────────────────────────────────────────
[Q] {GolgiApparatus.name} - {"🧬 "+str(GolgiApparatus.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{GolgiApparatus.dpc}

    The golgi apparatus is an organelle that sorts and delivers proteins to other
  parts of the cell, like a post office.
──────────────────────────────────────────────────────────────────────────────────────
[W] {Centrosome.name} - {"🧬 "+str(Centrosome.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Centrosome.dpc} DNA/click

    The centrosome is a small part of the cytoplasm that makes microtubules. It
  contains two structures called centrioles, that are made of short microtubules.
──────────────────────────────────────────────────────────────────────────────────────
[E] {Mitochondria.name} - {"🧬 "+str(Mitochondria.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Mitochondria.dpc} DNA/click

    The mitochondria is the powerhouse of the cell. It is a bean shaped organelle with
  an inner and outer membrane that supplies energy to the rest of the cell.
──────────────────────────────────────────────────────────────────────────────────────
[R] {Nucleolus.name} - {"🧬 "+str(Nucleolus.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  +{Nucleolus.dpc} DNA/click

    The nucleolus is an organelle that is in the nucleus and creates ribosomes.
──────────────────────────────────────────────────────────────────────────────────────
[T] {Nucleus.name} - {"🧬 "+str(Nucleus.cost)}
──────────────────────────────────────────────────────────────────────────────────────
  x{Nucleus.multiplier} DNA/click

    The nucleus is the organelle that contains the nucleoulus and produces DNA, allowing the cell to reproduce. 
  '''
  print(shopScreen)
  key = getkey()
  if key == "\t":
    game()
  elif key == "s":
    save()
    shop()
  elif key == "1":
    processPurchase(Flagellum, "add")
  elif key == "2":
    processPurchase(Cilium, "add")
  elif key == "3":
    processPurchase(CellMembrane, "add")
  elif key == "4":
    processPurchase(CellWall, "add")
  elif key == "5":
    processPurchase(Vacuole, "add")
  elif key == "6":
    processPurchase(Chloroplast, "add")
  elif key == "7":
    processPurchase(Ribosome, "add")
  elif key == "8":
    processPurchase(Cytoplasm, "add")
  elif key == "9":
    processPurchase(RoughER, "add")
  elif key == "0":
    processPurchase(SmoothER, "add")
  elif key == "q":
    processPurchase(GolgiApparatus, "add")
  elif key == "w":
    processPurchase(Centrosome, "add")
  elif key == "e":
    processPurchase(Mitochondria, "add")
  elif key == "r":
    processPurchase(Nucleolus, "add")
  elif key == "t":
    processPurchase(Nucleus, "multiply")
  else:
    shop()


def save():
  data = json.dumps({
    "dpc": str(dpc),
    "dna": str(dna),
    "orgCount": str(orgCount),
    "inventory": inventory
  })
  with open(f"saves/{name}.json", "w") as f:
    f.write(data)


game()