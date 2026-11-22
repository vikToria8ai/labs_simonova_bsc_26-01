from __future__ import annotations

import argparse
import sys
from typing import List

from num_series import (
    two_harmonics_series,
    summarize,
    simple_moving_average,
    exponential_moving_average,
)


# ---
# Фабрика ряда
# ---
def build_series(n: int, seed: int) -> List[float]:
    return two_harmonics_series(n, seed=seed)


# ---
# Печать
# ---
def print_series(title: str, values: List[float], fmt: str = "{:>10.3f}") -> None:
    print(f"\n{title} (n={len(values)}):")
    print(" " + " ".join(fmt.format(v) for v in values))


def print_header(n: int) -> None:
    print("=" * 60)
    print(f"Ряд: две гармоники, n = {n}")
    print("-" * 60)


def print_stats(stats: dict) -> None:
    print(f"Среднее арифметическое : {stats['mean']:>10.4f}")
    print(f"Медиана                : {stats['median']:>10.4f}")
    print(f"Размах (max - min)     : {stats['spread']:>10.4f}")
    print(f"min / max              : {stats['min']:>10.4f} / {stats['max']:>10.4f}")
    print(f"Число экстремумов      : {stats['extrema']:>10d}")


def print_footer() -> None:
    print("=" * 60)


# ---
# Разбор аргументов
# ---
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Алгоритмическая обработка числовых рядов (Вариант 11)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--n", type=int, default=1000,
        help="количество точек в ряде",
    )
    parser.add_argument(
        "--windows", type=int, nargs="+", default=[5, 25, 75],
        help="список размеров окна для SMA",
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="зерно ГПСЧ для воспроизводимости",
    )
    return parser


# ---
# main
# ---
def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        data = build_series(args.n, args.seed)
        stats = summarize(data)

        # Предупреждение, если окно слишком велико относительно ряда
        warnings = []
        for w in args.windows:
            if w > args.n:
                warnings.append(
                    f"окно {w} больше длины ряда {args.n} — SMA невозможна"
                )
                continue
            if w >= args.n // 2:
                warnings.append(
                    f"окно {w} слишком велико относительно n={args.n} — ряд сильно сгладится"
                )

        # Считаем SMA для валидных окон
        sma_results = {}
        for w in args.windows:
            if 1 <= w <= args.n:
                sma_results[w] = simple_moving_average(data, w)

        # EMA с alpha = 2/(k+1) для каждого окна (по заданию Варианта 11)
        ema_results = {}
        for w in args.windows:
            if w >= 1:
                alpha = 2.0 / (w + 1)
                ema_results[w] = exponential_moving_average(data, alpha)

    except ValueError as err:
        print(f"Ошибка: {err}", file=sys.stderr)
        return 1

    print_header(args.n)
    print_stats(stats)

    for w in warnings:
        print(f"ВНИМАНИЕ: {w}")

    print_series("Исходный ряд", data)

    for w, sma in sma_results.items():
        print_series(f"SMA (window={w})", sma)

    for w, ema in ema_results.items():
        alpha = 2.0 / (w + 1)
        print_series(f"EMA (window={w}, alpha={alpha:.4f})", ema)

    print_footer()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())