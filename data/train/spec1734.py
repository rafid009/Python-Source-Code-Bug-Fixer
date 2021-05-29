import numpy as np 

def function(x):

	i5 = x
	g3 = 8
	x = 6
	paths = []
	try:
		if i5 < 3:
			i5 = 8*i5
			paths.append(1)
		else:
			x = g3-3
			x = 8+2
			x = i5/x
			paths.append(2)
		if x <= 1:
			g3 = g3-g3
			g3 = 3+g3
			x = 4*x
			paths.append(3)
		else:
			x = 0-x
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