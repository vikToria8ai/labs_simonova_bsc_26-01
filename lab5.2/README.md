# num_series_app — Вариант 11

Модульное консольное приложение для обработки числовых рядов.

Ряд: две гармоники
`x[i] = 3*sin(0.05*i) + 0.5*cos(0.3*i) + uniform(-0.2, 0.2)`, `i = 0..n-1`.

## Структура

- `num_series/` — пакет
  - `generator.py` — формирование числовых рядов (включая `two_harmonics_series`)
  - `stats.py` — среднее, медиана, размах, число экстремумов
  - `moving_average.py` — SMA, центрированное MA, EMA
  - `io_json.py` — сохранение и чтение JSON
  - `io_file.py` — чтение txt/csv
- `main.py` — CLI

## Запуск

```bash
python main.py --n 1000 --windows 5 25 75 --seed 42