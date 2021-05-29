import numpy as np 

def function(x):

	d1 = 0
	g7 = x
	paths = []
	try:
		if d1 > 4:
			d1 = 1-6
			g7 = 9+g7
			d1 = d1-1
			paths.append(1)
		else:
			g7 = 4-0
			paths.append(2)
		if x <= 2:
			d1 = d1+9
			paths.append(3)
		else:
			d1 = 2+6
			d1 = 7-1
			g7 = g7+g7
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