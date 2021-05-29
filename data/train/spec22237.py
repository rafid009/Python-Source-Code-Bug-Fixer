import numpy as np 

def function(x):

	b1 = x
	g0 = x
	paths = []
	try:
		if x > 2:
			g0 = 7*g0
			x = 7-x
			paths.append(1)
		else:
			g0 = g0*b1
			x = 6-g0
			g0 = 0/g0
			paths.append(2)
		if g0 >= 6:
			b1 = 8+b1
			x = x/b1
			b1 = b1+9
			paths.append(3)
		else:
			b1 = g0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))