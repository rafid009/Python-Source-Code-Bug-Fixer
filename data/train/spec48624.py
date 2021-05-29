import numpy as np 

def function(x):

	g1 = 9
	u1 = x
	paths = []
	try:
		if x <= 8:
			x = 7+x
			paths.append(1)
		else:
			g1 = 8/g1
			u1 = 2-u1
			g1 = g1*6
			paths.append(2)
		if g1 < 1:
			g1 = g1/7
			u1 = u1+u1
			paths.append(3)
		else:
			g1 = 7*4
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