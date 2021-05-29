import numpy as np 

def function(x):

	i7 = x
	g0 = x
	x = 7
	paths = []
	try:
		if g0 > 1:
			x = 3/i7
			g0 = 4*g0
			paths.append(1)
		else:
			g0 = g0+6
			g0 = g0/9
			g0 = g0+x
			paths.append(2)
		if i7 > 7:
			g0 = 1/i7
			paths.append(3)
		else:
			g0 = g0/1
			x = g0-2
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))