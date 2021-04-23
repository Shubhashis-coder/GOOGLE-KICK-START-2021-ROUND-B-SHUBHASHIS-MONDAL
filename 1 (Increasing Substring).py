import sys

input = sys.stdin.readline

def solve():
	n = int(input())
	b = 'A'
	L = 0
	for i in input().strip():
		if i > b:
			L += 1
		else:
			L = 1
		b = i
		print(L, end=' ')
	print()

for i in range(int(input())):
	print('Case #'+str(i+1),end=': ')
	solve()
