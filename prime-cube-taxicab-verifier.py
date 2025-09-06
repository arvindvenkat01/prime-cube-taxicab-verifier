# MIT License
#
# Copyright (c) 2025 Arvind N. Venkat
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import math
import numpy as np
from numba import njit
import time

@njit
def sieve_primes_numba(limit):
    if limit < 2:
        return np.empty(0, dtype=np.int64)
    is_prime = np.ones(limit + 1, dtype=np.bool_)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = np.empty(limit, dtype=np.int64)
    count = 0
    for i in range(limit + 1):
        if is_prime[i]:
            primes[count] = i
            count += 1
    return primes[:count]

def is_perfect_square(n):
    if n < 0:
        return False, 0
    sqrt_n = math.isqrt(n)  # Python 3.8+ arbitrary precision integer sqrt
    if sqrt_n * sqrt_n == n:
        return True, sqrt_n
    else:
        return False, 0

def elegant_search(max_prime=100000):
    primes = sieve_primes_numba(max_prime)
    if len(primes) < 3:
        return []
    solutions = []
    for i in range(len(primes) - 2):
        # Convert to Python int to avoid overflow on large cubics
        p1, p2, p3 = int(primes[i]), int(primes[i+1]), int(primes[i+2])
        n_squared = p2**3 + p3**3 - p1**3  # Python int handles large integer arithmetic safely
        if n_squared <= 0:
            continue
        is_int, n = is_perfect_square(n_squared)
        if is_int:
            ratio = n / p1
            solutions.append({
                'p1': p1,
                'p2': p2,
                'p3': p3,
                'n': n,
                'ratio': ratio,
                'sum': p2**3 + p3**3
            })
    return solutions

def analyze_results(solutions):
    if not solutions:
        print("No solutions found.")
        return
    print(f"Found {len(solutions)} solution(s):")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}: {sol['p1']}³ + {sol['n']}² = {sol['p2']}³ + {sol['p3']}³ = {sol['sum']}")
        print(f"  Consecutive primes: ({sol['p1']}, {sol['p2']}, {sol['p3']})")
        print(f"  Ratio n/p1 = {sol['ratio']:.6f}")
        gap1 = sol['p2'] - sol['p1']
        gap2 = sol['p3'] - sol['p2']
        print(f"  Prime gaps: {gap1}, {gap2}")
    if len(solutions) >= 2:
        ratios = [sol['ratio'] for sol in solutions]
        diffs = [ratios[i+1] - ratios[i] for i in range(len(ratios)-1)]
        if all(abs(d - 1.0) < 0.001 for d in diffs):
            print("Pattern detected: Ratios are consecutive integers.")

if __name__ == "__main__":
    print("Starting elegant search for consecutive prime triples...")
    max_prime = 10000000000  # Adjust as needed; be cautious with large values due to runtime
    start = time.time()
    solutions = elegant_search(max_prime)
    elapsed = time.time() - start
    print(f"Completed search up to prime {max_prime} in {elapsed:.2f} seconds.")
    analyze_results(solutions)
