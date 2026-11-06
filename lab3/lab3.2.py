text = input("Введите строку: ")

error = ""

if text == "":
    error = "вы ничего не ввели"
elif text.strip() == "":
    error = "строка состоит только из пробелов"
else:
    has_letter = False

    for symbol in text:
        if symbol.isalpha():
            has_letter = True

    if has_letter == False:
        error = "в строке нет ни одной буквы"

if error != "":
    print("Ошибка:", error)
else:
    max_length = 0
    current_length = 0

    for symbol in text:
        if symbol == "н" or symbol == "Н":
            current_length += 1

            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 0

    new_text = text.replace("!", ".")

    print("Длина самой длинной последовательности «н»:", max_length)
    print("Строка после замены:", new_text)
