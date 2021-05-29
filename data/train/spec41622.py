import numpy as np 

def function(x):

	d6 = x
	g6 = 7
	paths = []
	try:
		if x < 7:
			x = d6*d6
			paths.append(1)
		else:
			x = 4*x
			d6 = d6-8
			g6 = 4-g6
			paths.append(2)
		if d6 < 7:
			d6 = d6*8
			paths.append(3)
		else:
			g6 = g6/3
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))