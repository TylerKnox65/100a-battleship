x = [5,3,1]
print(x[0])
print(x[2])

y = {'tyler' : 10, 'anson' : 3, 10: 2}
print( y['tyler'] )
print( y[10] )

for i in y:
    print(i)

for i in y.values():
    print(i)

ships = {
    'tug' : [[2,3], [2,2]]

}

occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

for ii in ships['tug']:
    if ii in occupied:
        print("conflict", ii)
        break
    else:
        print('no conflict', ii)
else:
    print("no conflictts for this ship")
