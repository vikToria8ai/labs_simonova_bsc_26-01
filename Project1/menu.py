"""
Меню выбора типа насоса 
"""
from __future__ import annotations

from connstanta import N_1, N_2, N_3

def show_menu()  -> None:
    """Вывести меню тип насоса."""
    print("\n Выберите тип насоса:")
    print("  1 — центробежный  (k = 0.75)")
    print("  2 — поршневой     (k = 0.85)")
    print("  3 — вихревой      (k = 0.55)")
    print("  0 — выход")

def select_mode() -> float | None:
      while True:
        choice = input("Введите номер класса (от 0 до 3): ").strip()
        match choice:
            case "1":
                return N_1
            case "2":
                return N_2
            case "3":
                return N_3
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")

def mode_name(n: float) -> str:
    """Вернуть название режима по коэффициенту n."""
    match n:
        case 1.0:
            return "центробежный "
        case 0.85:
            return "поршневой"
        case 0.7:
            return "вихревой"
        case _:
            return "неизвестный"