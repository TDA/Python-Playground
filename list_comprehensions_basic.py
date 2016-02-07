__author__ = 'saipc'

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],]

print(matrix)
x = []
for row in matrix:
    x.extend(row)
print(x)
odd_nos = [elt for elt in x if elt % 2 == 1]
print(odd_nos)
