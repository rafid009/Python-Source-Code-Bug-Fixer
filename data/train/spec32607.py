import numpy as np 

def function(x):

	x7 = 4
	x0 = x
	paths = []
	try:
		if x <= 3:
			x7 = 2/5
			x7 = 6*x7
			x = x-6
			paths.append(1)
		else:
			x0 = x7-x7
			x7 = x0+x
			paths.append(2)
		if x0 < 4:
			x7 = x7+6
			x0 = x7*x0
			paths.append(3)
		else:
			x7 = 1/7
			x = x+9
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