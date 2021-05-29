import numpy as np 

def function(x):

	e6 = x
	j4 = 8
	x = 8
	paths = []
	try:
		if e6 <= 2:
			x = 3/1
			paths.append(1)
		else:
			j4 = x-4
			j4 = e6*j4
			e6 = 1/e6
			paths.append(2)
		if e6 < 2:
			x = x-5
			paths.append(3)
		else:
			j4 = 9-j4
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