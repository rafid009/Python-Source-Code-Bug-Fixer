import numpy as np 

def function(x):

	g6 = x
	i1 = x
	paths = []
	try:
		if x < 9:
			x = g6/2
			x = x+8
			i1 = i1/g6
			paths.append(1)
		else:
			i1 = 1-6
			paths.append(2)
		if x > 0:
			x = x/9
			paths.append(3)
		else:
			g6 = 8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))