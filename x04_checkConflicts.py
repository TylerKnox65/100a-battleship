#!python3

'''
##### 4. Check for conflicts
It is not possible for a boat to occupy the same space as another boat.  
We would need to add a tool to check to see if a boat that we are trying 
to place is overlapping with another boat, so that if it is, we can re-create it.

One strategy:
Create a function that converts all existing boats to a list of coordinates and add them to
a list of "occupied" squares
Check each of your new ship squares to see if there is a conflict
The two functions that have been created here might be helpful
'''
from x03create import positions  




def fullList(ships):
  Horizontal = False
  Vertical = False
  xCoord = ships[0]
  yCoord = ships[1]
  try:
    # Horizontal [x],[y, y, y]
    Slength = len(ships[1])
    Horizontal = True
  except:
    #Vertical [x, x, x],y
    Slength = len(ships[0])
    Vertical = True
  
  if Slength == 2:
    if Vertical == True:
      coord1 = [xCoord[0], yCoord]
      coord2 = [xCoord[1], yCoord]
    if Horizontal == True:
      coord1 = [xCoord, yCoord[0]]
      coord2 = [xCoord, yCoord[1]]
    coordOCC = [coord1, coord2]
  elif Slength == 3:
    if Vertical == True:
      coord1 = [xCoord[0], yCoord]
      coord2 = [xCoord[1], yCoord]
      coord3 = [xCoord[2], yCoord]
    if Horizontal == True:
      coord1 = [xCoord, yCoord[0]]
      coord2 = [xCoord, yCoord[1]]
      coord3 = [xCoord, yCoord[2]]
    coordOCC = [coord1, coord2, coord3]


  elif Slength == 4:
    if Vertical == True:
      coord1 = [xCoord[0], yCoord]
      coord2 = [xCoord[1], yCoord]
      coord3 = [xCoord[2], yCoord]
      coord4 = [xCoord[3], yCoord]

    if Horizontal == True:
      coord1 = [xCoord, yCoord[0]]
      coord2 = [xCoord, yCoord[1]]
      coord3 = [xCoord, yCoord[2]]
      coord4 = [xCoord, yCoord[3]]

    coordOCC = [coord1, coord2, coord3, coord4]
  elif Slength == 5:
    if Vertical == True:
      coord1 = [xCoord[0], yCoord]
      coord2 = [xCoord[1], yCoord]
      coord3 = [xCoord[2], yCoord]
      coord4 = [xCoord[3], yCoord]
      coord5 = [xCoord[4], yCoord]
    if Horizontal == True:
      coord1 = [xCoord, yCoord[0]]
      coord2 = [xCoord, yCoord[1]]
      coord3 = [xCoord, yCoord[2]]
      coord4 = [xCoord, yCoord[3]]
      coord5 = [xCoord, yCoord[4]]
    coordOCC = [coord1, coord2, coord3, coord4, coord5]
  
  return coordOCC



  
  
  '''
  inputs:
  ships: list of all current/valid ship data
  
  return:
  list of occupied coordinates
  (example: [ [0,2] , [0,3] , [1,4] , [2,4] , [3,4] ])

  '''
  '''
  inputs:
  occupied: list of all occupied squares
  boat: dictionary with information about your boat you are checking
  
  return: 
  True if the new boat conflicts with existing data
  False if the new boat does not conflict
  '''
   

  
def isConflict(boat1,boat2):

  for i in boat1:
    if i in boat2:
      return True
    else:
      pass
  
        #HELP
  return False
  

Tug = fullList(positions(3))
Sub = fullList(positions(4))
Destroyer = fullList(positions(4))
Carrier = fullList(positions(5))
Battleship = fullList(positions(6))
print(f"{Tug}\n{Sub}\n{Destroyer}\n{Carrier}\n{Battleship}\n")

def check(x):
  global Tug, Sub, Destroyer, Carrier, Battleship
  while True:
    if x == Tug:
      Check1 = isConflict(x, Sub)
      if Check1 == False:
        Check2 = isConflict(x, Destroyer)
        if Check2 == False:
          Check3 = isConflict(x, Carrier)
          if Check3 == False:
            Check4 = isConflict(x, Battleship)
            if Check4 == False:
              break
            else:
              Battleship = fullList(positions(6))
          else:
            Carrier = fullList(positions(5)) 
        else:
          Destroyer = fullList(positions(4))
      else:
        Sub = fullList(positions(4))
    elif x == Sub:
      Check1 = isConflict(x, Tug)
      if Check1 == False:
        Check2 = isConflict(x, Destroyer)
        if Check2 == False:
          Check3 = isConflict(x, Carrier)
          if Check3 == False:
            Check4 = isConflict(x, Battleship)
            if Check4 == False:
              break
            else:
              Battleship = fullList(positions(6))
          else:
            Carrier = fullList(positions(5)) 
        else:
          Destroyer = fullList(positions(4))
      else:
        Tug = fullList(positions(3)) 
    elif x == Destroyer:
          Check1 = isConflict(x, Tug)
          if Check1 == False:
              Check2 = isConflict(x, Sub)
              if Check2 == False:
                Check3 = isConflict(x, Carrier)
                if Check3 == False:
                  Check4 = isConflict(x, Battleship)
                  if Check4 == False:
                    break
                  else:
                    Battleship = fullList(positions(6))
                else:
                  Carrier = fullList(positions(5)) 
              else:
                Sub = fullList(positions(4))
          else:
              Tug = fullList(positions(3)) 
    elif x == Carrier:
      Check1 = isConflict(x, Tug)
      if Check1 == False:
        Check2 = isConflict(x, Destroyer)
        if Check2 == False:
          Check3 = isConflict(x, Sub)
          if Check3 == False:
            Check4 = isConflict(x, Battleship)
            if Check4 == False:
              break
            else:
              Battleship = fullList(positions(6))
          else:
            Sub = fullList(positions(5)) 
        else:
          Destroyer = fullList(positions(4))
      else:
        Tug = fullList(positions(3)) 
    elif x == Battleship:
      Check1 = isConflict(x, Tug)
      if Check1 == False:
        Check2 = isConflict(x, Destroyer)
        if Check2 == False:
          Check3 = isConflict(x, Carrier)
          if Check3 == False:
            Check4 = isConflict(x, Sub)
            if Check4 == False:
              break
            else:
              Sub = fullList(positions(6))
          else:
            Carrier = fullList(positions(5)) 
        else:
          Destroyer = fullList(positions(4))
      else:
        Tug = fullList(positions(3)) 
  return None





Tug = fullList(positions(3))
Sub = fullList(positions(4))
Destroyer = fullList(positions(4))
Carrier = fullList(positions(5))
Battleship = fullList(positions(6))
x = 10000
while x > 0:
  check(Tug)
  check(Sub)
  check(Destroyer)
  check(Carrier)
  check(Battleship)
  x -= 1 #A Goofy way to sort... Just pray and hope that it works. It works most of the time I swear
print(f"{Tug}\n{Sub}\n{Destroyer}\n{Carrier}\n{Battleship}\n")
