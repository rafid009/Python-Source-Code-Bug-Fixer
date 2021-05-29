import numpy as np 

def function(x):

	b9 = 8
	g0 = x
	paths = []
	try:
		if b9 > 2:
			g0 = g0*g0
			g0 = 4+4
			g0 = 5-g0
			paths.append(1)
		else:
			b9 = b9/4
			paths.append(2)
		if g0 <= 4:
			b9 = 1*x
			g0 = 1/x
			x = 5-b9
			paths.append(3)
		else:
			g0 = 4/g0
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