import itertools
import math
print("Num of func :")
N = int(input())
print("Dostupnie :")
K = int(input())

vozm = list(range(1, N+1))

print("PORYADOK\n")

arrange = list(itertools.product(vozm, repeat =K))
c_arr = len(arrange)
formula = N**K
print(f"Vsego: {c_arr}")
print(f"Formula: {formula}")

print("MESS")

comb = list(itertools.combinations_with_replacement(vozm, K))
c_comb = len(comb)

print(f"Vsego: {c_comb}")
print(f"Formula: {math.factorial(N+K-1) // (math.factorial(K) * math.factorial(N-1))}")
