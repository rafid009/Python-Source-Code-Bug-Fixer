import numpy as np 

def function(x):

	v1 = x
	g4 = x
	paths = []
	try:
		if x > 2:
			v1 = 1*4
			paths.append(1)
		else:
			g4 = 0-g4
			paths.append(2)
		if v1 >= 0:
			x = 1+5
			paths.append(3)
		else:
			v1 = g4-v1
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