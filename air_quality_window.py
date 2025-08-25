"""
Algoritmos para Janela de Qualidade do Ar (Desafio 2)
- Brute Force
- Divide and Conquer
- Dynamic Programming (Kadane's Algorithm)
"""
import time
from utils import timer

@timer
def brute_force(scores):
    n = len(scores)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            s = sum(scores[i:j+1])
            if s > max_sum:
                max_sum = s
    return max_sum

@timer
def divide_and_conquer(scores):
    def max_subarray(l, r):
        if l == r:
            return scores[l]
        m = (l + r) // 2
        left = max_subarray(l, m)
        right = max_subarray(m+1, r)
        cross = max_crossing(l, m, r)
        return max(left, right, cross)
    def max_crossing(l, m, r):
        left_sum = float('-inf')
        s = 0
        for i in range(m, l-1, -1):
            s += scores[i]
            left_sum = max(left_sum, s)
        right_sum = float('-inf')
        s = 0
        for i in range(m+1, r+1):
            s += scores[i]
            right_sum = max(right_sum, s)
        return left_sum + right_sum
    return max_subarray(0, len(scores)-1)

@timer
def kadane(scores):
    max_sum = float('-inf')
    current_sum = 0
    for x in scores:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum
