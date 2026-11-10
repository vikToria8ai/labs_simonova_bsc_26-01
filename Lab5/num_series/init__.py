from .generator import random_series, sine_series, trend_series
from .stats import mean, median, spread, summarize
from .moving_average import (
    simple_moving_average,
    centered_moving_average,
    exponential_moving_average,
)

__all__ = [
    "random_series", "sine_series", "trend_series",
    "mean", "median", "spread", "summarize",
    "simple_moving_average",
    "centered_moving_average",
    "exponential_moving_average",
]

__version__ = "1.0.0"
