import numpy as np 

def function(x):

	y6 = 6
	w4 = x
	paths = []
	try:
		if x < 1:
			w4 = w4+4
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x <= 9:
			y6 = y6+x
			x = x+0
			paths.append(3)
		else:
			y6 = y6/8
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