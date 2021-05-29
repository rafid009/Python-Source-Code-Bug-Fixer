import numpy as np 

def function(x):

	g1 = x
	a8 = 5
	x = x
	paths = []
	try:
		if x < 9:
			g1 = g1/x
			x = x+2
			a8 = 4/a8
			paths.append(1)
		else:
			g1 = x*x
			a8 = a8+1
			x = x+6
			paths.append(2)
		if a8 <= 2:
			g1 = g1/3
			g1 = a8-7
			a8 = a8-4
			paths.append(3)
		else:
			a8 = a8*3
			g1 = g1*g1
			g1 = g1+1
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