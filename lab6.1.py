import itertools
import math
print("Contacts :")
N = int(input())
print("Num of dialogues :")
K = int(input())

contacts = list(range(1, N+1))

print("PORYADOK\n")

arrange = list(itertools.permutations(contacts, K))
c_arr = len(arrange)
print(f"Vsego: {c_arr}")
print(f"Formula: {math.factorial(N) // math.factorial(N-K)}")

print("MESS")

comb = list(itertools.combinations(contacts, K))
c_comb = len(comb)

print(f"Vsego: {c_comb}")
print(f"Formula: {math.factorial(N) // (math.factorial(K) * math.factorial(N-K))}")
