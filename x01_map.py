#! python3

"""
* Take a list of coordinates and draw a map showing occupied squares
* The map is a 10x10 grid
* (0,0) is the coordinate in the bottom left (like a regular (x,y) grid system)

```
Sample Data1:
[[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

Suggested Output:
..........
.xxxx.....
....x.....
....x.....
....x.....
....x.....
x...x.....
x.........
xxx.......
....xxx...

Sample Data2:
[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]

..........
........x.
.......xx.
xxxxx..xx.
.......x..
.x........
.x........
.x........
.x........
xx........
```
"""

occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]
grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]




def line():
    length = len(occupied)
    for i in range(length):
        base = 0
        while base != 1:
            coord = occupied[i]
            coordy = coord[1]
            coordx = coord[0]
            if grid[coordy][coordx] == 0:
                grid[coordy][coordx] = 1    
                base = 1
'''
def zerorep(x):
    for i in x[0]:
        if x[0][i] == 0:
            x[0][i] == "." 
        elif x[0][i] == 1:
            x[0][i] == "x"
'''     
#For replacing 0 with "." and 1 with "x", not needed.
        



def main():
    line()
    grid.reverse()
    #zerorep(grid)
    print(f"{grid[0]}\n{grid[1]}\n{grid[2]}\n{grid[3]}\n{grid[4]}\n{grid[5]}\n{grid[6]}\n{grid[7]}\n{grid[8]}\n{grid[9]}\n")
    #print(f"{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n{list[4]}\n{list[5]}\n{list[6]}\n{list[7]}\n{list[8]}\n{list[9]}\n")
main()