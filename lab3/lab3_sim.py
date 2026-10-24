#1
n = 0
fn = False

for p in range(100):
    if fn == False:
        try:
            v = int(input("Введите количество элементов в цепи: "))
            if v > 0:
                n = v
                fn = True  
            else:
                print("Количество должно быть больше 0")
        except ValueError:
            print("Вы ввели буквы. Нужно ввести целое число")

tR = 0
for i in range(1, n + 1):
    cR = 0.0
    fR = False 
    for pR in range(100):
        if fR == False:
            try:
                vR = float(input(f"Введите сопротивление {i}-го элемента (Ом): "))
                if vR >= 0:
                    cR = vR
                    fR = True  
                else:
                    print("Сопротивление не может быть отрицательным")
            except ValueError:
                print("Вы ввели буквы. Для дробей используйте точку")
    tR = tR + cR

print(f"Общее сопротивление цепи: {tR} Ом")


#2
N = 0
fN = False
for p in range(100):
    if fN == False:
        try:
            v = int(input("Введите целое число N (> 0): "))
            if v > 0:
                N = v
                fN = True  
            else:
                print("Число N должно быть строго больше нуля")
        except ValueError:
            print("Вы ввели буквы. Нужно ввести целое число")

if fN == True:
    K = 0
    while (K + 1) * (K + 1) <= N:
        K = K + 1
    print(f"Наибольшее целое число K: {K}")
else:
    print("Вы ввели не корректное число N")
