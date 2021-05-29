import numpy as np 

def function(x):

	v5 = 5
	g1 = x
	paths = []
	try:
		if g1 >= 0:
			g1 = v5*g1
			paths.append(1)
		else:
			g1 = g1+7
			v5 = 1*2
			g1 = g1*g1
			paths.append(2)
		if g1 >= 3:
			g1 = 2-g1
			v5 = 5/4
			x = x+x
			paths.append(3)
		else:
			x = 1*x
			g1 = 0+x
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