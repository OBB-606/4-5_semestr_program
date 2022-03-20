def array_line_search(array: list, array_size: int, desire_number: int):
    """
    Осуществляет линейный поиск числа в массиве от 0 до array_size -1 индекса включительно
    Возвращает индекс элемента в массиве
    Или "-1", если элемент не найден
    Если в массиве несколько одинаковых элементов, равных desire_number, то
    возвращается индекс первого из них
    :param array:
    :param array_size:
    :param desire_number:
    :return:
    """
    for i in range(array_size):
        if array[i] == desire_number:
            return i
    return -1


def test_array_line_search():
    array_1 = [1, 2, 3, 4, 5]
    m = array_line_search(array_1, 5, 8)
    if m == -1:
        print("#test_1 - ok")
    else:
        print("#test_1  - fail")


test_array_line_search()
