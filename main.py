
from validation import input_innings, input_pressure,input_density
from menu import show_menu, select_mode, mode_name
from operations import power_drive,pressure_class


def main() -> None:
    """Главный сценарий."""
    print("=== Расчёт мощьности  ===")

    while True:
        show_menu()
        n = select_mode()
        if n is None:
            print("Работа завершена.")
            break

        q= input_innings()
        h = input_pressure()
        pl= input_density()

        p = power_drive(q, h , pl ,n)
        cls = pressure_class(h)

        print("\n Результаты ")
        print(f"Тип насоса:     {mode_name(n)} (n = {n})")
        print(f"Мощьность напора (P):    {p:.2f} ")
        print(f"Подача насоса(Q):    {q} ")
        print(f"Напор насоса (H):   {h} ")
        print(f"Класс напора: {cls}")
        print("\n")


if __name__ == "__main__":
    main()