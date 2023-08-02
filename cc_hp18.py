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

def solve(n, nums, a, b):
    bob_m = alice_m = common_m = 0

    for num in nums:
        if num%a == 0 and num%b == 0:
            common_m += 1
        elif num%a == 0:
            bob_m += 1
        elif num%b == 0:
            alice_m += 1
    
    if common_m:
        bob_m += 1
        
    if bob_m > alice_m:
        print("BOB")
    else:
        print("ALICE")


if __name__ == "__main__":
    T = _int()

    while T > 0:
        n, a, b = _lst_int()
        nums = _lst_int()
        solve(n, nums, a, b)

        T -= 1
