import numpy as np 

def function(x):

	x7 = x
	e1 = 2
	x = 7
	paths = []
	try:
		if x >= 3:
			e1 = 5-0
			x7 = 3-x7
			x = x-0
			paths.append(1)
		else:
			x7 = x7/6
			x = 9/9
			paths.append(2)
		if x > 2:
			x = x-x
			x = x7/e1
			paths.append(3)
		else:
			x = 5/x
			x7 = x7+9
			x = 7/x
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