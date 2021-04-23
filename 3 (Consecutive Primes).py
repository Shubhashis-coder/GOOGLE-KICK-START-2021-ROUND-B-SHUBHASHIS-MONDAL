import sys

input = sys.stdin.readline

def is_prime(n):
	if n < 2:
		return False
	for i in range(2,n+1):
		if i * i > n:
			return True
		if n % i == 0:
			return False
	return True

def solve1(Z):
	p = 2
	best = 0
	for i in range(3, Z):
		if is_prime(i):
			if i * p > Z:
				break
			best = i * p
			p = i
	return best

def solve2(Z):
	q = int(Z**0.5)
	while q * q < Z:
		q += 1
	big = 0
	for i in range(q, Z):
		if is_prime(i):
			big = i
			break
	prev = 0
	for i in range(q-1, 1, -1):
		if is_prime(i):
			prev = i
			break
	if prev * big <= Z:
		return prev * big
	for i in range(prev - 1, 1, -1):
		if is_prime(i):
			return i * prev
	return None

def solve():
	Z = int(input())
	print(solve2(Z))

for i in range(int(input())):
	print('Case #'+str(i+1),end=': ')
	solve()
