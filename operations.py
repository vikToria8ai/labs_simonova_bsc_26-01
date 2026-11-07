"""
Расчёты: мощьность напора  P, класс напора.
"""
from typing import Annotated

from connstanta import G ,H_SMAL, H_LARGE

def cutting_speed(
    q: Annotated[float, "Подача , м3/м"],
    h: Annotated[float, "Напор, м"],
    pl: Annotated[float, "Плотность среды, кг/м3"],
    n: Annotated[float, "Тип насоса"],
) -> float:
    """
    Рассчитать мощьность напора  P = pl * g * q *h/(3600*n *1000), кВт.
    Args:
        q: Подача , м3/м
        h: Напор, м
        pl: Плотность среды, кг/м3
    """
    return pl * G * q *h / (3600* n *1000)


def diameter_class(
    h: Annotated[float, "Диаметр, мм"],
) -> str:
    """
    Классифицировать диаметр через if-elif-else.

    H < 10 — малый напор;
    10 ≤ H ≤ 60 — средний напор;
    H > 60 — высокий напор.

    Args:
        h: напор, м.

    Returns:
        Строка с названием класса напора.
    """
    if h < H_SMALL:
        return "малый напор"
    elif h <= H_LARGE:
        return "средний напор"
    else:
        return "высокий напор"