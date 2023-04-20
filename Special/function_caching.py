# lru_cache is used to store the result previous computation in cache everytime program is executed
from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return 1
    time.sleep(5)
    return fib(n - 1) + fib(n - 2)


print(fib(4))
print("Done for 4.")
print(fib(5))
print("Done for 5.")
print(fib(6))
print("Done for 6.")

print(fib(4))
print("Done for 4.")
print(fib(5))
print("Done for 5.")
print(fib(6))
print("Done for 6.")
