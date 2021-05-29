import numpy as np 

def function(x):

	g0 = x
	a8 = 2
	paths = []
	try:
		if a8 <= 4:
			a8 = x+2
			a8 = 5*x
			a8 = 3/a8
			paths.append(1)
		else:
			g0 = 4/5
			g0 = 2*g0
			paths.append(2)
		if a8 < 8:
			g0 = g0+x
			g0 = x+9
			paths.append(3)
		else:
			a8 = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))