import numpy as np 

def function(x):

	g4 = 8
	u0 = x
	paths = []
	try:
		if x >= 3:
			x = x+4
			paths.append(1)
		else:
			x = 1/2
			u0 = u0+x
			paths.append(2)
		if u0 <= 3:
			g4 = x-g4
			paths.append(3)
		else:
			x = u0-x
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