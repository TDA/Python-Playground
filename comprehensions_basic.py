__author__ = 'saipc'

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],]


def even_filter(x):
    return x % 2 == 0

print(matrix)
x = []
for row in matrix:
    x.extend(row)
print(x)
odd_nos = [elt for elt in x if elt % 2 == 1]
print(odd_nos)

# with filter
even_nos = filter(even_filter, x)
print(even_nos)

# map sums to rows:
sums = { i : sum(matrix[i]) for i in range(3)}
print(sums)