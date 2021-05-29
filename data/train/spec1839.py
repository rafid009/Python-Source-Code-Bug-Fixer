import numpy as np 

def function(x):

	r9 = 3
	b6 = 4
	paths = []
	try:
		if b6 > 8:
			b6 = 0/b6
			paths.append(1)
		else:
			r9 = x/4
			b6 = 3+1
			r9 = 7+r9
			paths.append(2)
		if b6 >= 7:
			b6 = x*b6
			r9 = r9-8
			b6 = 2+b6
			paths.append(3)
		else:
			r9 = x*8
			x = x-4
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))