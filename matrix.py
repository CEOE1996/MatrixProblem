import re

n, m = input("").strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input(""))
    matrix.append(matrix_t)

Decoded = ""

for y in range(m):
    for x in range(n):
        Decoded += matrix[x][y]

Decoded = re.sub('(?<=\w)\W+(?=\w)', ' ', Decoded)

print(Decoded)
