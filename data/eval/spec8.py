import numpy as np 

def function(x):

	g1 = 5
	d1 = x
	paths = []
	try:
		if d1 <= 7:
			d1 = d1-5
			x = x-3
			paths.append(1)
		else:
			x = x*g1
			x = 2-1
			g1 = g1+d1
			paths.append(2)
		if x > 4:
			x = g1+g1
			paths.append(3)
		else:
			x = x-3
			x = x-2
			x = x-g1
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