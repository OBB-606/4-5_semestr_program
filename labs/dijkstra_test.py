import math


def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i

def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 1, 3, 0, 0),
    (3, 0, 4, 0, 0, 0),
    (1, 4, 0, 0, 7, 5),
    (3, 0, 0, 0, 0, 2),
    (0, 0, 7, 0, 0, 4),
    (0, 0, 5, 2, 4, 0))

N = len(D)
T = [math.inf]*N

v = 0
S = {v}
T[v] = 0

while v != -1:
    for j in get_link_v(v, D):
        if j not in S:
            w = T[v] + D[v][j]
            if w < T[j]:
                T[j] = w

    v = arg_min(T, S)
    if v > 0:
        S.add(v)

print(T)