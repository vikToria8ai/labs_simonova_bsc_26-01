def find_max_even():
  while True:
    user_input = input("Введите целые числа через пробел: ")

    try:
      numbers = [int(item) for item in user_input.split()]
      if not numbers:
        print("Список пустой. Пожалуйста, введите хотя бы одно число.")
        continue
      break
    except ValueError:
      print("Вы ввели неверные данные. Используйте только целые числа через пробел.")

  even_numbers = [num for num in numbers if num % 2 == 0]

  if not even_numbers:
    print("В списке нет ни одного четного числа, делящегося на 2 без остатка.")
  else:
    max_even = max(even_numbers)
    print(f"Наибольшее четное число в списке: {max_even}")


if __name__ == "__main__":
  find_max_even()
