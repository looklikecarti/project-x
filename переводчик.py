from random import *
from itertools import *
true_v = []
null = lambda x, y, z, w: True if (x == (w or y)) or ((not w or z) and (not y or w)) else False # (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w)).
act = True
while act:
    f = [randint(0,1) for i in range(4)]
    if null(f[0], f[1], f[2], f[3]) == False and f not in true_v and len(true_v) < 4:true_v.append(f)
    if len(true_v) == 4:
        for t in true_v:shuffle(t)
        s = sample(true_v, 3)
        for ind, val in enumerate(permutations([h for h in range(4)])):
            if null(s[0][val[0]], s[0][val[1]], s[0][val[2]], s[0][val[3]]) == False and s[0][0] == 1 and s[0][3] == 1:
                if null(s[1][val[0]], s[1][val[1]], s[1][val[2]], s[1][val[3]]) == False and s[1][3] == 1:
                    if null(s[2][val[0]], s[2][val[1]], s[2][val[2]], s[2][val[3]]) == False and s[2][0] == 1 and s[2][2] == 1:
                        for i in s:print(i)
                        print(f"otvet: x = {val[0] + 1}; y = {val[1] + 1}; z = {val[2] + 1}; w = {val[3] + 1}")
                        act = False
        s.clear()