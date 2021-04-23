import sys
from math import gcd

input = sys.stdin.readline

def solve():
	N, Q = map(int, input().split())
	SZ = 1
	while SZ < N:
		SZ *= 2
	T = [0]*(SZ*2)
	R = [None]*(N-1)
	P = [None] * N
	G = [[] for i in range(N)]
	for i in range(N-1):
		X, Y, Li, Ai = map(int, input().split())
		X -= 1
		Y -= 1
		R[i] = (Li, X, Y, Ai)
		G[X].append(Y)
		G[Y].append(X)
	q = [0]
	idx = []
	P[0] = -1
	tout = [-1]*N
	tin = [-1]*N
	while len(q):
		x = q.pop()
		tin[x] = len(idx)
		idx.append(x)
		for v in G[x]:
			if P[v] is None:
				P[v] = x
				q.append(v)
	#print(P)
	for i in range(len(idx)-1, -1, -1):
		v = idx[i]
		tout[v] = max(tout[v], i)
		if P[v] >= 0:
			tout[P[v]] = max(tout[P[v]], tout[v])
	#print(idx)
	#print(tin)
	#print(tout)
	ans = [None]*Q
	for i in range(Q):
		Cj, Wj = map(int, input().split())
		R.append((Wj, N + i, Cj - 1, Wj))
	R.sort()
	for W, X, Y, Ai in R:
		if X >= N:
			#print('get', W,X-N,Y)
			#print(T)
			Y = tin[Y] + SZ
			r = 0
			while Y >= 1:
				r = gcd(r, T[Y])
				Y //= 2
			#print('=',r)
			ans[X-N] = r
		else:
			#print('add', W,X,Y,Ai)
			if P[X] == Y:
				l = tin[X] + SZ
				r = tout[X] + SZ
			else:
				l = tin[Y] + SZ
				r = tout[Y] + SZ
			#print(l, r)
			while l <= r:
				#print('lr',l, r)
				if l % 2 == 1:
					T[l] = gcd(T[l], Ai)
				if r % 2 == 0:
					T[r] = gcd(T[r], Ai)
				l = (l + 1)//2
				r = (r - 1)//2
			#print(T)
	print(' '.join(map(str,ans)))

for i in range(int(input())):
	print('Case #'+str(i+1),end=': ')
	solve()
