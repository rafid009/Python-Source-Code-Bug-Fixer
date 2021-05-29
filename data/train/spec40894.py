import numpy as np 

def function(x):

	g6 = 6
	i8 = 7
	paths = []
	try:
		if g6 <= 9:
			i8 = 8*4
			paths.append(1)
		else:
			x = x/g6
			x = x-3
			i8 = 2*i8
			paths.append(2)
		if x >= 6:
			g6 = 5+g6
			x = x-i8
			x = x+9
			paths.append(3)
		else:
			g6 = 0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))