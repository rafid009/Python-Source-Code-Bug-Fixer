import numpy as np 

def function(x):

	g6 = 2
	n7 = x
	x = x
	paths = []
	try:
		if x < 8:
			x = 7+x
			x = x/2
			g6 = g6+4
			paths.append(1)
		else:
			n7 = n7/6
			g6 = 2/g6
			paths.append(2)
		if x > 9:
			g6 = n7+6
			paths.append(3)
		else:
			n7 = n7*1
			x = x-g6
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