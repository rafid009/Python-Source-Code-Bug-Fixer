import numpy as np 

def function(x):

	l8 = 6
	g0 = 7
	paths = []
	try:
		if x <= 8:
			g0 = l8-4
			paths.append(1)
		else:
			g0 = g0*g0
			paths.append(2)
		if l8 < 3:
			x = x/3
			l8 = 2*7
			l8 = l8-9
			paths.append(3)
		else:
			l8 = l8/1
			l8 = l8*3
			x = x+9
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