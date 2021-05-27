import numpy as np 

def function(x):

	v3 = x
	g0 = 9
	paths = []
	try:
		if g0 <= 8:
			g0 = g0+0
			x = x-g0
			paths.append(1)
		else:
			g0 = 1/v3
			paths.append(2)
		if x > 4:
			g0 = v3/g0
			g0 = x+x
			g0 = x*g0
			paths.append(3)
		else:
			v3 = x-9
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