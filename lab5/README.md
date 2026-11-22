# num_series_app

Модульное консольное приложение для алгоритмической обработки числовых рядов.

## Структура

- `num_series/` — пакет
  - `generator.py` — формирование числовых рядов
  - `stats.py` — среднее, медиана, размах
  - `moving_average.py` — SMA, центрированное MA, EMA
  - `io_json.py` — сохранение и чтение JSON
  - `io_file.py` — чтение txt/csv
- `main.py` — CLI

## Запуск

```bash
python main.py --kind sine --n 20 --window 3 --alpha 0.3 --seed 7