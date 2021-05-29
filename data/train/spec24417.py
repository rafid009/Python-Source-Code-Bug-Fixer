import numpy as np 

def function(x):

	a8 = x
	y6 = x
	paths = []
	try:
		if a8 < 3:
			x = 2*y6
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if a8 > 3:
			x = x+8
			y6 = y6/y6
			paths.append(3)
		else:
			y6 = y6*3
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