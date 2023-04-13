#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """
  coordinate = coordinate.strip()
  coordinate = coordinate.upper()
  coordinate = coordinate.replace(" ", "")
  coordlist = [*coordinate]

  length = len(coordlist)
  if length == 3:
    charident(coordlist)
    coordlist.pop(-1)
    coordlist[1] = 9
    return coordlist
  else:
    charident(coordlist)
    coordlist[1] = int(coordlist[1])
    #coordlist = [eval(i) for i in coordlist]
    x = coordlist[1] - 1
    coordlist[1] = x
  return coordlist

def charident(x):
  if x[0] == "A":
    x[0] = 0
    return x 
  elif x[0] == "B":
    x[0] = 1
    return x
  elif x[0] == "C":
    x[0] = 2
    return x
  elif x[0] == "D":
    x[0] = 3
    return x
  elif x[0] == "E":
    x[0] = 4
    return x
  elif x[0] == "F":
    x[0] = 5
    return x
  elif x[0] == "G":
    x[0] = 6
    return x
  elif x[0] == "H":
    x[0] = 7
    return x
  elif x[0] == "I":
    x[0] = 8
    return x
  elif x[0] == "J":
    x[0] = 9
    return x


if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  
