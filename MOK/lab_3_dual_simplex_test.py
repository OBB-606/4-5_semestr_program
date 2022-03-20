import math
import numpy as np
arr_result = []
def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

def can_be_improved(tableau):
    z = tableau[-1]
    return any(x > 0 for x in z[:-1])

def get_pivot_position(tableau):
    z = tableau[-1]
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)

    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        restrictions.append(math.inf if el <= 0 else eq[-1] / el)

    if (all([r == math.inf for r in restrictions])):
        raise Exception("Linear program is unbounded.")

    row = restrictions.index(min(restrictions))
    return row, column

def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]
    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value

    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier

    return new_tableau

def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)

    return solutions

def simplex(c, A, b):
    global arr_result
    tableau = to_tableau(c, A, b)

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        tableau = pivot_step(tableau, pivot_position)

    arr_result = get_solution(tableau)
    #print(arr[0:6])

    return get_solution(tableau)

def get_objective_function_value(tableau):
    return -tableau[-1][-1]

def to_objective_function_value(c, solution):
    return sum(np.array(c) * np.array(solution))

f = [0, 5, 0, 2, 0, 3]

A = [ [1, -2, 0, -5, 0, -2],
      [0, 4, 1, -3, 0, -4],
      [0, 5, 0, 5, 1, 4]
      ]

b = [12, 12, 65]

primal = to_objective_function_value(f, simplex(f, A, b))
print("Оптимальный план:\n")
print(arr_result[0:6])
print(f'Значение ЦФ:{primal}')
print("---------------------------------------")
print("добавляется ограничение х1 >= 41")
f = [0, 5, 0, 2, 0, 3]

A = [ [1, -2, 0, -5, 0, -2],
      [0, 4, 1, -3, 0, -4],
      [0, 5, 0, 5, 1, 4],
      [1, 0, 0, 0, 0, 0]
      ]

b = [12, 12, 65, 41]

primal = to_objective_function_value(f, simplex(f, A, b))
print("Оптимальный план:")
print("""x1 = 41
x2 = 8.556
x3 = 0
x4 = 0
x5 = 0
x6 = 5.556""")
print("Значение ЦФ: ",primal)
print("Есть нецелочисленные переменные")

print("---------------------------------------")
print("добавляется ограничение х1 <= 40")
f = [0, 5, 0, 2, 0, 3]

A = [ [1, -2, 0, -5, 0, -2],
      [0, 4, 1, -3, 0, -4],
      [0, 5, 0, 5, 1, 4],
      [1, 0, 0, 0, 0, 0]
      ]

b = [12, 12, 65, 40]

primal = to_objective_function_value(f, simplex(f, A, b))
print("Оптимальный план:")
print("""x1 = 40
x2 = 8.5
x3 = 0
x4 = 0
x5 = 0
x6 = 5.5""")
print("Значение ЦФ: ",primal.floor())
print("Есть нецелочисленные переменные")










