import numpy as np 

def function(x):

	x8 = x
	e4 = 8
	paths = []
	try:
		if x8 < 3:
			x = 3/x
			x = x*4
			paths.append(1)
		else:
			x8 = 6/x
			e4 = 2-e4
			e4 = e4*6
			paths.append(2)
		if x8 <= 9:
			x = x/e4
			e4 = 1*e4
			paths.append(3)
		else:
			x8 = x+x
			x = 1*x
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