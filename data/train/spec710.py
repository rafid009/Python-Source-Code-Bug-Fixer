import numpy as np 

def function(x):

	g1 = 5
	a0 = x
	paths = []
	try:
		if a0 > 0:
			x = x+x
			a0 = g1+x
			g1 = g1+6
			paths.append(1)
		else:
			g1 = g1*a0
			g1 = 4+g1
			x = g1+x
			paths.append(2)
		if a0 < 4:
			g1 = 5*5
			x = x+0
			paths.append(3)
		else:
			a0 = a0+1
			g1 = 4-g1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))