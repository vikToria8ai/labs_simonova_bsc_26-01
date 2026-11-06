def process_array():
    is_valid_input = False
    array = []

    while not is_valid_input:
        user_input = input("Введите элементы массива (целые числа через пробел): ")
        try:
            array = [int(item) for item in user_input.split()]
            if len(array) > 0:
                is_valid_input = True
            else:
                print("Массив пустой. Попробуйте еще раз.")
        except ValueError:
            print("Ошибка! Вводите только целые числа через пробел.")

    # Фильтруем: число должно быть четным И меньше 10
    filtered_array = [num for num in array if num % 2 == 0 and num < 10]

    if len(filtered_array) == 0:
        print("Таких чисел нет.")
    else:
        filtered_array.sort()
        print("Полученный массив в порядке возрастания:", filtered_array)

if __name__ == "__main__":
    process_array()
