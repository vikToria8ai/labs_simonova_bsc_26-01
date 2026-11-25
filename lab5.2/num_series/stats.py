from typing import Dict, Sequence


def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")


def mean(data: Sequence[float]) -> float:
    """Среднее арифметическое."""
    _ensure_not_empty(data)
    return sum(data) / len(data)


def median(data: Sequence[float]) -> float:
    """Медиана (устойчива к выбросам)."""
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0


def spread(data: Sequence[float]) -> float:
    """Размах ряда: max - min."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))


def count_extrema(data: Sequence[float]) -> int:
    """Число экстремумов (локальных максимумов и минимумов)

    Точка i (0 < i < n-1) — экстремум, если она строго больше или
    строго меньше обоих соседей.
    """
    _ensure_not_empty(data)
    if len(data) < 3:
        return 0
    count = 0
    for i in range(1, len(data) - 1):
        left, cur, right = data[i - 1], data[i], data[i + 1]
        if (cur > left and cur > right) or (cur < left and cur < right):
            count += 1
    return count


def summarize(data: Sequence[float]) -> Dict[str, float]:
    """Сводный отчёт: count, mean, median, spread, min, max, extrema."""
    _ensure_not_empty(data)
    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "spread": spread(data),
        "min": float(min(data)),
        "max": float(max(data)),
        "extrema": count_extrema(data),
    }