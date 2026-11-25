from os import PathLike
from pathlib import Path
from typing import List


def _parse_numbers(text: str, sep: str = ",") -> List[float]:
    cleaned = text.replace(sep, " ").replace(";", " ").replace(",", " ")
    tokens = cleaned.split()
    if not tokens:
        raise ValueError("Не найдено ни одного числа")
    result: List[float] = []
    for i, tok in enumerate(tokens):
        try:
            result.append(float(tok))
        except ValueError as err:
            raise ValueError(
                f"Элемент {i} = {tok!r} не является числом"
            ) from err
    return result


def load_series_txt(path: PathLike) -> List[float]:
    file_path = Path(path)
    if not file_path.exists():
        raise ValueError(f"Файл не найден: {file_path}")
    result: List[float] = []
    try:
        with file_path.open("r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    result.append(float(line))
                except ValueError as err:
                    raise ValueError(
                        f"Строка {lineno} = {line!r} не является числом"
                    ) from err
    except OSError as err:
        raise ValueError(f"Не удалось прочитать файл {file_path}: {err}") from err
    if not result:
        raise ValueError(f"Ряд в файле {file_path} пуст")
    return result


def load_series_csv(path: PathLike, sep: str = ",") -> List[float]:
    file_path = Path(path)
    if not file_path.exists():
        raise ValueError(f"Файл не найден: {file_path}")
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError as err:
        raise ValueError(f"Не удалось прочитать файл {file_path}: {err}") from err
    return _parse_numbers(text, sep=sep)