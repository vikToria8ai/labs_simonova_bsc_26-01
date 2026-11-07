import math

# --- Тип насоса ---
N_1: float = 0.75    # центробежный 
N_2: float = 0.85     # поршневой 
N_3: float = 0.55   # вихревой 

# --- Допустимые диапазоны входных данных ---
Q_MIN: float = 0.5
Q_MAX: float = 500.0
H_MIN: float = 1.0
H_MAX: float = 200.0
Pl_MIN: float = 800.0
Pl_MAX: float = 1200.0

# --- Пороговые значения для классификации напора  ---
H_SMALL: float = 10.0     # H < 10 — малый
H_LARGE: float = 60.0     # H > 60 — высокий

# --- Ускорение свободного падения  ---
G= 9.81

# --- Файл журнала ошибок ---
LOG_FILE: str = "input_errors.log"

