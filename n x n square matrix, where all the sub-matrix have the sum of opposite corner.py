import itertools
def sub_mat_even(n):
	
	temp = itertools.count(1)
	l = [[next(temp)for i in range(n)]for i in range(n)]
	if n%2 == 0:
		for i in range(0,len(l)):
			if i%2 == 1:
				l[i][:] = l[i][::-1]
	for i in range(n):
		for j in range(n):
			print(l[i][j],end=" ")
		print()

n = 4
sub_mat_even(n)
