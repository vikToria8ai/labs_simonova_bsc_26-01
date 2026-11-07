from __future__ import annotations

from connstanta import H_MIN, H_MAX, Q_MIN, Q_MAX , Pl_MIN, Pl_MAX
from logger import log_error

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """
    Проверка попадания value в [low, high] через if-elif-else.
    :return: (True, "") или (False, сообщение)
    """
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""

def input_number(prompt: str, low: float, high: float) -> float:
    """
    Циклически запрашивать число, пока не будет корректного.
    Проверяет тип (float) через try/except ValueError и границы.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)

def input_diameter() -> float:
    """Циклический ввод напора насоса H (м), допустимо 1..200."""
    return input_number(
        "Введите напор насоса H, м (1..200): ",
        H_MIN, H_MAX,
    )

def input_frequency() -> float:
    """Циклический ввод подачи насоса  Q (м3/ч), допустимо 0.5..500."""
    return input_number(
        "Введите подачи насоса  Q, м3/ч (0.5..500): ",
        Q_MIN, Q_MAX,
    )

def input_frequency() -> float:
    """Циклический ввод плотности среды  Pl (кг/м3), допустимо 800..1200."""
    return input_number(
        "Введите плотности среды  Pl (кг/м3) (800..1200):",
        Pl_MIN, Pl_MAX,
    )