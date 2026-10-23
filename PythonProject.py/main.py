Q = float(input("Введите подачу Q (от 0.5 до 500 м^3/ч): "))
H = float(input("Введите напор H (от 1 до 200 м): "))
r = float(input("Введите плотность среды rho (от 800 до 1200 кг/м^3): "))

g = 9.81

if H < 10:
    head_class = "малый напор"
elif 10 <= H <= 60:
    head_class = "средний"
else:
    head_class = "высокий"

pump_types = ["центробежный", "поршневой", "вихревой"]
es = [0.75, 0.85, 0.55]

print("\n--- Результаты расчета ---")

for i in range(3):
    pump_type = pump_types[i]
    e = es[i]

    P = (r * g * Q * H) / (3600 * e * 1000)
    
    print(f"Тип: {pump_type} , Q: {Q} м3/ч ,  H: {H} м ({head_class}) , Мощность: {round(P, 2)} кВт")

