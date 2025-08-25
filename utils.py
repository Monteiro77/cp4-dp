"""
Funções auxiliares e decorators para medição de tempo e qualidade de software.
"""
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Tempo de execução de {func.__name__}: {(end-start)*1000:.2f} ms")
        return result
    return wrapper
