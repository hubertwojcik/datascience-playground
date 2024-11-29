import random
from typing import List
from collections import Counter

num_friends = [random.randint(1, 100) for _ in range(204)]

def mean(xs:List[float])->float:
    return sum(xs) / len(xs)

def _median_odd(xs: List[float])->float:
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float])->float:
    sorted_xs = sorted(xs)
    mid_point = len(xs) // 2
    return (sorted_xs[mid_point - 1] + sorted_xs[mid_point]) / 2

def median(v: List[float])->float:
    return _median_even(v) if len(v) % 2 ==0 else _median_odd(v)

def quantile(xs: List[float], p:float)-> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

def mode(xs: List[float])-> List[float]:
    counts = Counter(xs)
    print(counts.items())
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

