import numpy as np 

def function(x):

	g0 = x
	r5 = 6
	paths = []
	try:
		if r5 > 9:
			g0 = g0/2
			paths.append(1)
		else:
			g0 = g0*9
			g0 = g0*5
			paths.append(2)
		if x <= 7:
			g0 = 9*g0
			paths.append(3)
		else:
			r5 = 9/r5
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