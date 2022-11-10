def to_int_if_digit(input_str):
    no_space_str = input_str.replace(" ", "").replace(' ', "").strip()
    if no_space_str.isdigit():
        return int(no_space_str)
    else:
        print("Введено не число!")
        return False


def split_input_numbers(input_numbers_str):
    local_input_str = input_numbers_str.strip()
    while (" " not in local_input_str) or (not to_int_if_digit(local_input_str)):
        local_input_str = input("Введите последовательность целых чисел через пробел: ").strip()

    return [to_int_if_digit(i) for i in local_input_str.split()]


def sort_by_asc(numbers_list):
    for i in range(1, len(numbers_list)):
        key = numbers_list[i]
        j = i-1
        while numbers_list[j] > key and j >= 0:
            numbers_list[j + 1] = numbers_list[j]
            j -= 1
        numbers_list[j + 1] = key
    return numbers_list


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False

        middle = (right+left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle-1)
        else:
            return binary_search(array, element, middle+1, right)
    except IndexError:
        return "Число выходит за границы диапазона"


def find_right_index(numbers_list, compare_number):
    bigger_number = [x for x in numbers_list if x >= compare_number]

    if len(bigger_number) > 0:
        return numbers_list.index(bigger_number[0])
    else:
        return "Не найден"


def find_left_index(numbers_list, compare_number):
    bigger_index = find_right_index(numbers_list, compare_number)
    if (type(bigger_index) is int) and (bigger_index > 0):
        return int(bigger_index) - 1
    else:
        return "Не найден"


input_numbers = split_input_numbers(input("Введите последовательность целых чисел через пробел: "))
main_number = input("Введите число для сравнения: \n")
while not to_int_if_digit(main_number):
    main_number = input("Введите число для сравнения: \n")

main_number = to_int_if_digit(main_number)


sorted_list = sort_by_asc(input_numbers)
print(f'Отсортированный список (по-возрастанию): {sorted_list}')
binary_search_rez = binary_search(sorted_list, main_number, 0, len(sorted_list))

if binary_search_rez:
    print(f'Индекс введенного элемента: {binary_search_rez}')
else:
    print(f'Введенное число не найдено в списке\n'
          f'Индекс меньшего числа: {find_left_index(sorted_list, main_number)}\n'
          f'Индекс большего числа: {find_right_index(sorted_list, main_number)}\n')
