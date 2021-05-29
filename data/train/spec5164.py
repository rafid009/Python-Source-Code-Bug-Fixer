import numpy as np 

def function(x):

	g6 = x
	d2 = x
	paths = []
	try:
		if d2 <= 5:
			g6 = g6*7
			x = x/4
			x = 7*x
			paths.append(1)
		else:
			d2 = d2/d2
			g6 = g6+9
			x = x-x
			paths.append(2)
		if x > 9:
			g6 = 6/6
			g6 = g6-d2
			g6 = 2+g6
			paths.append(3)
		else:
			g6 = 5-g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))