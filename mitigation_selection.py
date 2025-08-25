"""
Algoritmos para Seleção de Projetos de Mitigação (Desafio 1)
- Brute Force
- Divide and Conquer (Meet-in-the-Middle)
- Dynamic Programming (Bottom-Up)
"""
import itertools
import time
from utils import timer

@timer
def brute_force(projects, budget):
    n = len(projects)
    max_benefit = 0
    best_subset = []
    for r in range(n+1):
        for subset in itertools.combinations(projects, r):
            cost = sum(p[0] for p in subset)
            benefit = sum(p[1] for p in subset)
            if cost <= budget and benefit > max_benefit:
                max_benefit = benefit
                best_subset = subset
    return max_benefit, best_subset

@timer
def meet_in_the_middle(projects, budget):
    n = len(projects)
    half = n // 2
    left = projects[:half]
    right = projects[half:]
    left_subsets = [(sum(p[0] for p in subset), sum(p[1] for p in subset)) for r in range(len(left)+1) for subset in itertools.combinations(left, r)]
    right_subsets = [(sum(p[0] for p in subset), sum(p[1] for p in subset)) for r in range(len(right)+1) for subset in itertools.combinations(right, r)]
    right_subsets.sort()
    max_benefit = 0
    for lc, lb in left_subsets:
        remain = budget - lc
        candidates = [rb for rc, rb in right_subsets if rc <= remain]
        if candidates:
            total_benefit = lb + max(candidates)
            if total_benefit > max_benefit:
                max_benefit = total_benefit
    return max_benefit

@timer
def dp_bottom_up(projects, budget):
    n = len(projects)
    dp = [0] * (budget + 1)
    for cost, benefit in projects:
        for b in range(budget, cost-1, -1):
            dp[b] = max(dp[b], dp[b-cost] + benefit)
    return dp[budget]
