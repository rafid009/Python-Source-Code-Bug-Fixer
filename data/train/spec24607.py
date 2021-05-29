import numpy as np 

def function(x):

	g0 = 5
	r2 = x
	paths = []
	try:
		if g0 < 4:
			x = x+1
			paths.append(1)
		else:
			g0 = 9+4
			paths.append(2)
		if g0 <= 1:
			g0 = g0-1
			paths.append(3)
		else:
			r2 = r2*g0
			g0 = 3+g0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))