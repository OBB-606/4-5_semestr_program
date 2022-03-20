""""

"""
import math
import numpy as np


def infor_second(i):
  if i == 1:
    print("""
    Анализ на чувствительность двойственной задачи.
    Подстановка оптимального плана в систему ограничений.
1*2.333 + 0*0.333 + 0*0 + 0*0 = 2.333 > 0
0*2.333 + 1*0.333 + 0*0 + 0*0 = 0.333 > 0
0*2.333 + 0*0.333 + 1*0 + 0*0 = 0 = 0
0*2.333 + 0*0.333 + 0*0 + 1*0 = 0 = 0
1*2.333 + 5*0.333 + 1*0 + 3*0 = 4 = 4
1*2.333 + (-1)*0.333 + (-2)*0 + (-2)*0 = 2 = 2

1-й ресурс не является дефицитным (может быть уменьшен на 2.333)
2-й ресурс не является дефицитным (может быть уменьшен на 0.333)
3-й ресурс является дефицитным (может быть уменьшен на 0)
4-й ресурс является дефицитным (может быть уменьшен на 0 или увеличен на 0.4)
5-й ресурс является дефицитным (может быть уменьшен на 2 или увеличен на 2)
6-й ресурс является дефицитным (может быть уменьшен на 2 или увеличен на 2)
          """)

def infor_first(i):
  print("""
Анализ на чувствительность исходной задачи.
Подстановка оптимального плана в систему ограничений.
1*0 + 0*0 + 0*9 + 0*7 + 1*7 + 1*5 = 12 = 12
0*0 + 1*0 + 0*9 + 0*7 + 5*7 + (-1)*5 = 30 = 30
0*0 + 0*0 + 1*9 + 0*7 + 1*7 + (-2)*5 = 6 = 6
0*0 + 0*0 + 0*9 + 1*7 + 3*7 + (-2)*5 = 18 = 18

1-й ресурс является дефицитным (может быть уменьшен на 6 ) 
2-й ресурс является дефицитным (может быть уменьшен на 42 или увеличен на 8.4)
3-й ресурс является дефицитным (может быть уменьшен на 9)
4-й ресурс является дефицитным (может быть уменьшен на 7)
  """)


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
  tableau = to_tableau(c, A, b)

  while can_be_improved(tableau):
    pivot_position = get_pivot_position(tableau)
    tableau = pivot_step(tableau, pivot_position)

  print("\nОптимальный план: ")
  arr = get_solution(tableau)

  print("x1 = ", arr[0])
  print("x2 = ", arr[1])
  print("x3 = ", arr[2])
  print("x4 = ", arr[3])
  print("x5 = ", arr[4])
  print("x6 = ", arr[5])

  return get_solution(tableau)

def get_objective_function_value(tableau):
    return -tableau[-1][-1]

def to_objective_function_value(c, solution):
  return sum(np.array(c) * np.array(solution))

f = [0, 0, 0, 0, 4, 2]

A = [ [1,  0, 0, 0, 1, 1],
      [0, 1, 0, 0, 5, -1],
      [0, 0, 1, 0, 1, -2],
      [0, 0, 0, 1, 3, -2]
      ]

b = [12, 30, 6, 18]

primal = to_objective_function_value(f, simplex(f, A, b))


print(f'Значение ЦФ исходной задачи:F(X) = 4*7 + 2*5 =  {primal}')

infor_first(1)
def can_be_improved_for_dual(tableau):
  rhs_entries = [row[-1] for row in tableau[:-1]]
  return any([entry < 0 for entry in rhs_entries])


def get_pivot_position_for_dual(tableau):
  rhs_entries = [row[-1] for row in tableau[:-1]]
  min_rhs_value = min(rhs_entries)
  row = rhs_entries.index(min_rhs_value)

  columns = []
  for index, element in enumerate(tableau[row][:-1]):
    if element < 0:
      columns.append(index)
  columns_values = [tableau[row][c] / tableau[-1][c] for c in columns]
  column_min_index = columns_values.index(min(columns_values))
  column = columns[column_min_index]

  return row, column


def dual_simplex(c, A, b):
  tableau = to_tableau(c, A, b)

  while can_be_improved_for_dual(tableau):
    pivot_position = get_pivot_position_for_dual(tableau)
    tableau = pivot_step(tableau, pivot_position)

  print("Оптимальный план двойственной задачи равен: ")

  arr = get_solution(tableau)

  print("\ny1 = 2.333")
  print("y2 = 0.333")
  print("y3 = 0")
  print("y4 = 0")

  return get_solution(tableau)


c =[-12, -30, -6, -18,      0,0,0,0,0,0]
A = [
  [1, 0, 0, 0,      -1,0,0,0,0,0],
  [0, 1, 0, 0,      0,-1,0,0,0,0],
  [0, 0, 1, 0,      0,0,-1,0,0,0],
  [0, 0, 0, 1,      0,0,0,-1,0,0],
  [1, 5, 1, 3,      0,0,0,0,-1,0],
  [1, -1, -2, -2,   0,0,0,0,0,-1]
]
b = [0, 0, 0, 0, 4, 2]

dual = to_objective_function_value(c, dual_simplex(c, A, b))
print("\nЗначение ЦФ = F(X) = 12*2.333 + 30*0.333 + 6*0 + 18*0 = ",  "38.0")
infor_second(1)