import numpy as np 

def function(x):

	r7 = x
	g0 = x
	paths = []
	try:
		if r7 <= 6:
			r7 = 6-3
			paths.append(1)
		else:
			r7 = 3*r7
			x = g0*x
			r7 = 0-r7
			paths.append(2)
		if r7 >= 1:
			r7 = x-r7
			r7 = r7*x
			r7 = 5*r7
			paths.append(3)
		else:
			r7 = r7/2
			r7 = 4/3
			g0 = g0/3
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))