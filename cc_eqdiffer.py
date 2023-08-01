"""
    CodeChef EQDIFFER
    https://www.codechef.com/problems/EQDIFFER
"""

import os
import sys

sys.setrecursionlimit(100000000)

from sys import stdin, stdout
from statistics import mean, median, mode, variance
from math import pow, sqrt, gcd, lcm, factorial, perm, comb, ceil, floor, log, log2, log10
from collections import Counter as ctr, deque as dq, defaultdict as dd, OrderedDict as od
from bisect import bisect_left as bl, bisect_right as br

_fflush = lambda: stdout.flush()
_stdr = lambda: stdin.readline()
_stdw  = lambda x: stdout.write(str(x))

_str = lambda: input().strip()
_int = lambda: int(input().strip())
_flt = lambda: float(input().strip())

_lst_str = lambda: list(input().strip().split())
_lst_int = lambda: list(map(int,input().strip().split()))
_lst_flt = lambda: list(map(float,input().strip().split()))

MOD = 1000000007


def solve(N, A):
    if N < 3:
        print(0)
        return
    
    _max = max(ctr(A).values())
    print(N - max(_max, 2))


if __name__ == "__main__":
    T = _int()

    while T > 0:
        N = _int()
        A = _lst_int()
        solve(N, A)

        T -= 1
