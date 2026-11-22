from .generator import (
    random_series, sine_series, trend_series, two_harmonics_series,
)
from .stats import mean, median, spread, summarize, count_extrema
from .moving_average import (
    simple_moving_average,
    centered_moving_average,
    exponential_moving_average,
)
from .io_json import save_series_json, load_series_json
from .io_file import load_series_txt, load_series_csv

__all__ = [
    "random_series", "sine_series", "trend_series", "two_harmonics_series",
    "mean", "median", "spread", "summarize", "count_extrema",
    "simple_moving_average",
    "centered_moving_average",
    "exponential_moving_average",
    "save_series_json", "load_series_json",
    "load_series_txt", "load_series_csv",
]

__version__ = "1.1.0"