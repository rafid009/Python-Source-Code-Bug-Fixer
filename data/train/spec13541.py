import numpy as np 

def function(x):

	d6 = x
	g6 = 2
	paths = []
	try:
		if d6 < 6:
			g6 = g6*4
			d6 = d6*x
			g6 = g6+8
			paths.append(1)
		else:
			d6 = d6-4
			g6 = 3/5
			paths.append(2)
		if d6 >= 9:
			g6 = g6+9
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))