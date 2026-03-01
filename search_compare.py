from __future__ import annotations
import random, time
from typing import List, Tuple

TARGET_NOT_FOUND = 99_999_999

def sequential_search(data: List[int], target: int) -> Tuple[bool, float]:
    start = time.perf_counter()
    pos, found = 0, False
    while pos < len(data) and not found:
        if data[pos] == target:
            found = True
        else:
            pos += 1
    return found, time.perf_counter() - start

def ordered_sequential_search(data: List[int], target: int) -> Tuple[bool, float]:
    # data must be sorted before calling
    start = time.perf_counter()
    pos, found, stop = 0, False, False
    while pos < len(data) and not found and not stop:
        if data[pos] == target:
            found = True
        else:
            if data[pos] > target:
                stop = True
            else:
                pos += 1
    return found, time.perf_counter() - start

def binary_search_iterative(data: List[int], target: int) -> Tuple[bool, float]:
    # data must be sorted before calling
    start = time.perf_counter()
    first, last, found = 0, len(data) - 1, False
    while first <= last and not found:
        mid = (first + last) // 2
        if data[mid] == target:
            found = True
        else:
            if target < data[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found, time.perf_counter() - start

def _binary_search_recursive_helper(data: List[int], target: int, first: int, last: int) -> bool:
    if first > last:
        return False
    mid = (first + last) // 2
    if data[mid] == target:
        return True
    elif target < data[mid]:
        return _binary_search_recursive_helper(data, target, first, mid - 1)
    else:
        return _binary_search_recursive_helper(data, target, mid + 1, last)

def binary_search_recursive(data: List[int], target: int) -> Tuple[bool, float]:
    # data must be sorted before calling
    start = time.perf_counter()
    found = _binary_search_recursive_helper(data, target, 0, len(data) - 1)
    return found, time.perf_counter() - start

def benchmark_once(n: int, value_range: int = 50_000) -> Tuple[float, float, float, float]:
    data = [random.randint(1, value_range) for _ in range(n)]
    _, t_seq = sequential_search(data, TARGET_NOT_FOUND)
    sorted_data = sorted(data)  # sorting done outside the timed functions
    _, t_ord_seq = ordered_sequential_search(sorted_data, TARGET_NOT_FOUND)
    _, t_bin_it = binary_search_iterative(sorted_data, TARGET_NOT_FOUND)
    _, t_bin_rec = binary_search_recursive(sorted_data, TARGET_NOT_FOUND)
    return t_seq, t_ord_seq, t_bin_it, t_bin_rec

def average_times(list_size: int, runs: int = 100) -> Tuple[float, float, float, float]:
    total_seq = total_ord_seq = total_bin_it = total_bin_rec = 0.0
    for _ in range(runs):
        t_seq, t_ord_seq, t_bin_it, t_bin_rec = benchmark_once(list_size)
        total_seq += t_seq; total_ord_seq += t_ord_seq
        total_bin_it += t_bin_it; total_bin_rec += t_bin_rec
    return total_seq/runs, total_ord_seq/runs, total_bin_it/runs, total_bin_rec/runs

def main() -> None:
    for n in [500, 1000, 5000]:
        avg_seq, avg_ord_seq, avg_bin_it, avg_bin_rec = average_times(n, runs=100)
        print(f"\nList size: {n}")
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {avg_ord_seq:10.7f} seconds to run, on average")
        print(f"Binary Search (iterative) took {avg_bin_it:10.7f} seconds to run, on average")
        print(f"Binary Search (recursive) took {avg_bin_rec:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()