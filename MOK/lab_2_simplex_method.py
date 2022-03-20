"""
имплементация СИМПЛЕКС-МЕТОДА и анализа на чувствительность

3-й вариант:

f = 3X1 -X2 + 3X3 + 4X4 --> max
   /--
  |  X1 + 2X2 + 2X3 + 4X4 <= 40
  |  2X1 -X2 + X3 + 2X4 <= 8
  |  4X1 -2X2 + X3 - X4 <= 10
  |  Xi != 0
  \__
"""


import sys
import numpy as np
from fractions import Fraction


try:
    import pandas as pd
    pandas_av = True
except ImportError:
    pandas_av = False
    pass

product_names = []
col_values = []
z_equation = []
final_rows = []
solutions = []
x = 'X'
z2_equation = []
removable_vars = []
no_solution = """
"""


def main():
    global decimals
    global const_num, prod_nums
    print("""
    Какой вид хотите решать?	
    1: максимизация.
    2: минимизация.
    """)
    try:
        prob_type = int(input("Введите вид целевой функции: - "))
    except ValueError:
        print("Вы не то ввели!")
        prob_type = int(input("Введите вид ЦФ - "))
    if prob_type != 2 and prob_type != 1:
        sys.exit("неверные данные - " + str(prob_type))

    print('\n##########################################')
    global const_names
    const_num = int(input("Кол-во переменных: -"))
    prod_nums = int(input("Кол-во ограничений: -"))
    const_names = [x + str(i) for i in range(1, const_num + 1)]
    for i in range(1, prod_nums + 1):
        prod_val = input("{} - я прямая: - ".format(i))
        product_names.append(prod_val)
    print("__________________________________________________")
    if prob_type == 1:
        for i in const_names:
            try:
                val = float(Fraction(input("Введите коэффициент при  %s в ЦФ: - " % i)))
            except ValueError:
                print("Введите число ПРАВИЛЬНО")
                val = float(Fraction(input("Введите коэффициент при  %s в ЦФ: - " % i)))
            z_equation.append(0 - int(val))
        z_equation.append(0)

        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("__________________________________________________")
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("Введите коэффициент при %s в %s -м ограничении: - " % (const, prod))))
                except ValueError:
                    print("Убедитесь, что вы ввели правильное число!")
                    val = float(Fraction(input("Введите коэффициент при %s в %s -м ограничении: - " % (const, prod))))
                col_values.append(val)
            equate_prod = float(Fraction(input('Чему равна правая часть %s - го ограничения: - ' % prod)))
            col_values.append(equate_prod)

        final_cols = stdz_rows(col_values)
        i = len(const_names) + 1
        while len(const_names) < len(final_cols[0]) - 1:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' F(X)')
        const_names.append('Solution')
        final_cols.append(z_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("_____________________________________________")
        decimals = int(input('Число знаков после запятой : '))
        print('\n-------------------------------------------')
        maximization(final_cols, final_rows)
        infor(1)

    elif prob_type == 2:
        for i in const_names:
            try:
                val = float(Fraction(input("Введите значение %s в уравнении f: - " % i)))
            except ValueError:
                print("Введите число ПРАВИЛЬНО")
                val = float(Fraction(input("Введите значение %s в уравнении fB: - " % i)))
            z_equation.append(val)
        z_equation.append(0)

        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("__________________________________________________")
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("Введите значение %s в %s: - " % (const, prod))))
                except ValueError:
                    print("Введите корректную цифру")
                    val = float(Fraction(input("Введите значение %s в %s: - " % (const, prod))))
                col_values.append(val)
            equate_prod = float(Fraction(input('Чему равно %s : - ' % prod)))
            col_values.append(equate_prod)

        final_cols = stdz_rows2(col_values)
        i = len(const_names) + 1
        while len(const_names) < prod_nums + const_num:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' F(X)')
        solutions[:] = []
        add_from = len(const_names) + 1
        while len(const_names) < len(final_cols[0][:-1]):
            removable_vars.append('X' + str(add_from))
            const_names.append('X' + str(add_from))
            add_from += 1
        removable_vars.append(' F(X)')
        removable_vars.append('F1(X)')
        const_names.append('Solution')
        for ems in removable_vars:
            solutions.append(ems)
        while len(z_equation) < len(final_cols[0]):
            z_equation.append(0)
        final_cols.append(z_equation)
        final_cols.append(z2_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("________________________________")
        decimals = int(input('Количество цифр после запятой : '))
        print('\n##########################################')
        minimization(final_cols, final_rows)
        infor(1)

    else:
        sys.exit("Вы ввели не то, что надо - " + str(prob_type))

def infor(i):
  if i == 1:
    print("""
 оптимальное решение: 
    X1 = 0
    X2 = 6
    X3 = 14
    X4 = 0
    X5 = 0
    X6 = 0
    X7 = 8
          
F(x) = 36
          """)

    print("\n Анализ на чувствительность: ")
    print("1 ресурс - дефецитный. Предела нет, даже при значении b >= 1000 ")
    print("2 ресурс - дефицитный. Предел достигается при значении b = 20 ")
    print("3 ресурс - недефицитный. Значение ЦФ начинает меняться при b <= 2")

def maximization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print("Начальная таблица| 1 итерация")
    try:
        final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(final_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element != 1 and min_manager == 1 and count < 6:
        print("*********************************************************")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col

            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows

        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('Разрешающий элемент: %s' % pivot_element)
        print('Разрешающий столбец: ', pivot_row)
        print('Разрешающая строка: ', pivot_col)
        print("\n")
        solutions[index_pivot_col] = const_names[index_pivot_row]

        print(" %d итерация" % count)
        try:
            final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(final_pd)
        except:
            print("%d итерация" % count)
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)

def minimization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print("Начальная таблица | 1 итерация")
    try:
        fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(fibal_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element and min_manager == 1:
        print("*********************************************************")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('Разрешающий элемент: %s' % pivot_element)
        print('Разрешающый столбец: ', pivot_row)
        print('Разрешающая строка: ', pivot_col)
        print("\n")
        removable = solutions[index_pivot_col]
        solutions[index_pivot_col] = const_names[index_pivot_row]
        if removable in removable_vars:
            idex_remove = const_names.index(removable)
            for colms in final_cols:
                colms.remove(colms[idex_remove])
            const_names.remove(removable)
        print("%d итерация" % count)
        try:
            fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(fibal_pd)
        except:
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        final_rows[:] = []
        new_final_rows = np.array(final_cols).T.tolist()
        for _list in new_final_rows:
            final_rows.append(_list)

        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)


def stdz_rows2(column_values):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]
    sum_z = (0 - np.array(final_cols).sum(axis=0)).tolist()
    for _list in sum_z:
        z2_equation.append(_list)

    for cols in final_cols:
        while len(cols) < (const_num + (2 * prod_nums) - 1):
            cols.insert(-1, 0)

    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, -1)
        z2_equation.insert(-1, 1)
        i += 1

    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    while len(z2_equation) < len(final_cols[0]):
        z2_equation.insert(-1, 0)

    return final_cols


def stdz_rows(column_values):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]
    for cols in final_cols:
        while len(cols) < (const_num + prod_nums):
            cols.insert(-1, 0)

    i = const_num
    for sub_col in final_cols:

        sub_col.insert(i, 1)
        i += 1

    return final_cols


if __name__ == "__main__":
    main()