import sys

input = sys.stdin.readline

def solve():
	n = int(input())
	a = list(map(int,input().split()))
	b = [a[i] - a[i-1] for i in range(1,n)]
	p = [0]*(n-1)
	ne = [0]*(n-1)
	i = 0
	while i < len(b):
		v = b[i]
		j = i + 1
		while j < len(b):
			if b[j] != v:
				break
			j += 1
		for k in range(i, j):
			p[k] = i
			ne[k] = j-1
		i = j
	res = 1
	#print(b)
	#print(p)
	#print(ne)
	for i in range(1, len(b)):
		j = b[i] + b[i-1]
		if j % 2 == 0:
			j //= 2
			k = 2
			if i - 2 >= 0 and b[i - 2] == j:
				k += i - 2 - p[i - 2] + 1
			if i + 1 < len(b) and b[i + 1] == j:
				k += ne[i + 1] - (i + 1) + 1
			res = max(res, k)
		res = max(res, ne[i]-i+1+1)
		res = max(res, i-1-p[i-1]+1+1)
	print(res + 1)

for i in range(int(input())):
	print('Case #'+str(i+1),end=': ')
	solve()
