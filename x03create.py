#!python3

'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''
import random
def create():
  '''
  You will need to specify what information you need as inputs, but the output should be a list
  Add whatever code you need for each of your different ships to specify what coordinates it
  occupies and/or whether it is vertical/horizontal
  '''
  
  output = [
    { "name" : "Tugboat", "size" : 2 },
    { "name" : "Sumbarine", "size" : 3 },
    { "name" : "Destroyer", "size" : 3 },
    { "name" : "Carrier", "size" : 4 },
    { "name" : "Battelship", "size" : 5 }
    ]
  return output

def positions(size):
    output = create()
  #for i in range(5):
    
    
    hVSv = random.randint(0,1)
    if hVSv == 0:#Horiontal
      row = random.randint(0,9)
      colStart = random.randint(0,9)
      colEnd = colStart + size - 1
      #for i in range(10):
      if colEnd > 9:
          colEnd = colEnd - size + 1
          colStart = colStart - size + 1
      if colEnd <= 9 :
          occupied = [colStart, colEnd]
          occupiedFull = [row, occupied]
          tmp = list(range(occupied[0], occupied[1]))
          occupiedFull = [row, tmp]































      return occupiedFull
    elif hVSv == 1:#Vertical
      mCollumn = random.randint(0,9)
      rowstart = random.randint(0,9)
      rowend = rowstart + size - 1
      #for i in range(10):
      #if rowend == 9:

      if rowend > 9:
          rowend = rowend - size + 1
          rowstart = rowstart - size + 1
      if rowend <= 9 :
          occupied = [rowstart, rowend]
          occupiedFull = [occupied, mCollumn]
          tmp = list(range(occupied[0], occupied[1]))
          occupiedFull = [tmp, mCollumn]
      return occupiedFull
  


#Need size + 1 

#print(positions(6))
Tug = positions(3)
Sub = positions(4)
Destroyer = positions(4)
Carrier = positions(5)
Battleship = positions(6)