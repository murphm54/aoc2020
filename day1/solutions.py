import numpy as np
import os

print(os.getcwd())
txt = np.loadtxt("input.txt").astype(int)
res_one = None

for ind, i in enumerate(txt):
    if res_one is not None:
        break
    for j in np.delete(txt, ind):
        if i + j == 2020:
            res_one = i * j

print('Part 1 Answer: ', res_one)

res_two = None

for ind1, i in enumerate(txt):
    if res_two is not None:
        break
    for ind2, j in enumerate(txt):
        for k in np.delete(txt, (ind1, ind2)):
            if i + j + k == 2020:
                res_two = i * j * k

print('Part 2 Answer: ', res_two)
