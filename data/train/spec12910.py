import numpy as np 

def function(x):

	q9 = 9
	y0 = 9
	paths = []
	try:
		if x >= 3:
			q9 = 6/4
			y0 = y0/9
			x = x*x
			paths.append(1)
		else:
			x = x-x
			x = q9*x
			paths.append(2)
		if y0 >= 3:
			x = x-8
			paths.append(3)
		else:
			x = 9+8
			x = x*4
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