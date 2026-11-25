from typing import Sequence, List


def check_window(window: int, n: int) -> None:
    """Window — целое >= 1; window <= n (иначе окно больше ряда)."""
    try:
        is_positive_int = (window > 0) and (int(window) == window)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f"window должно быть положительным целым числом "
            f"(получено: {window!r}; причина: {err.args[0]})"
        ) from err

    if not is_positive_int:
        raise ValueError(
            f"window должно быть положительным целым числом (получено: {window!r})"
        )
    if window > n:
        raise ValueError(
            f"window не может быть больше длины ряда (получено: {window} > {n})"
        )


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA через бегущую сумму (O(n))."""
    check_window(window, len(data))
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result


def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное MA: окно нечётное, выход выровнен по центру."""
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"centered_moving_average требует нечётное окно (получено: {window})"
        )
    half = window // 2
    result = []
    for i in range(half, len(data) - half):
        chunk = data[i - half:i + half + 1]
        result.append(sum(chunk) / window)
    return result


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: EMA[0] = data[0]; EMA[i] = alpha*data[i] + (1-alpha)*EMA[i-1]."""
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    if not (0 < alpha <= 1):
        raise ValueError(
            f"alpha должно удовлетворять 0 < alpha <= 1 (получено: {alpha!r})"
        )
    result = [float(data[0])]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[i - 1])
    return result