import numpy as np 

def function(x):

	y5 = x
	e6 = 3
	paths = []
	try:
		if y5 >= 1:
			x = x*e6
			y5 = y5*y5
			e6 = e6/e6
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if e6 >= 9:
			y5 = 8+y5
			y5 = y5*e6
			paths.append(3)
		else:
			x = x/y5
			x = 3-y5
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