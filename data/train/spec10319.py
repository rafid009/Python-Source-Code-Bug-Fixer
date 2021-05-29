import numpy as np 

def function(x):

	n1 = 1
	g1 = 8
	paths = []
	try:
		if n1 < 8:
			g1 = g1+3
			g1 = 8*g1
			paths.append(1)
		else:
			n1 = n1*4
			x = x-8
			paths.append(2)
		if n1 < 6:
			x = 4-5
			paths.append(3)
		else:
			n1 = 3+x
			g1 = g1*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))