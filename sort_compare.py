from __future__ import annotations
import random, time
from typing import List, Tuple

def insertion_sort(data: List[int]) -> float:
    start = time.perf_counter()
    for index in range(1, len(data)):
        current_value = data[index]
        position = index
        while position > 0 and data[position - 1] > current_value:
            data[position] = data[position - 1]
            position -= 1
        data[position] = current_value
    return time.perf_counter() - start

def shell_sort(data: List[int]) -> float:
    start = time.perf_counter()
    gap = len(data) // 2
    while gap > 0:
        for start_pos in range(gap):
            i = start_pos + gap
            while i < len(data):
                current_value = data[i]
                j = i
                while j >= gap and data[j - gap] > current_value:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = current_value
                i += gap
        gap //= 2
    return time.perf_counter() - start

def python_sort(data: List[int]) -> float:
    start = time.perf_counter()
    data.sort()
    return time.perf_counter() - start

def benchmark_once(n: int, value_range: int = 50_000) -> Tuple[float, float, float]:
    base = [random.randint(1, value_range) for _ in range(n)]
    t_insert = insertion_sort(base.copy())
    t_shell  = shell_sort(base.copy())
    t_py     = python_sort(base.copy())
    return t_insert, t_shell, t_py

def average_times(list_size: int, runs: int = 100) -> Tuple[float, float, float]:
    total_insert = total_shell = total_py = 0.0
    for _ in range(runs):
        t_insert, t_shell, t_py = benchmark_once(list_size)
        total_insert += t_insert
        total_shell  += t_shell
        total_py     += t_py
    return total_insert/runs, total_shell/runs, total_py/runs

def main() -> None:
    sizes = [500, 1000, 5000]
    runs = 100
    for n in sizes:
        avg_insert, avg_shell, avg_py = average_times(n, runs=runs)
        print(f"\nList size: {n}")
        print(f"Insertion Sort took {avg_insert:10.7f} seconds to run, on average")
        print(f"Shell Sort took {avg_shell:10.7f} seconds to run, on average")
        print(f"Python sort() took {avg_py:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()