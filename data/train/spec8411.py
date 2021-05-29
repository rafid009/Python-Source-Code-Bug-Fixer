import numpy as np 

def function(x):

	g6 = 8
	i4 = x
	paths = []
	try:
		if x > 1:
			x = 0/i4
			paths.append(1)
		else:
			g6 = x/1
			paths.append(2)
		if x <= 5:
			g6 = g6+5
			g6 = g6/7
			g6 = g6-5
			paths.append(3)
		else:
			x = 2+i4
			g6 = 3-1
			g6 = g6-1
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