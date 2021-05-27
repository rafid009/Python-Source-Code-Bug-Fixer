import numpy as np 

def function(x):

	g1 = 5
	e7 = 2
	paths = []
	try:
		if x >= 7:
			g1 = g1+0
			paths.append(1)
		else:
			g1 = g1+5
			g1 = x/2
			paths.append(2)
		if x < 8:
			x = 6*2
			x = e7*x
			paths.append(3)
		else:
			x = 0*3
			g1 = 4*g1
			e7 = e7-7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		g1 = e7**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))