import numpy as np 

def function(x):

	v4 = 5
	u3 = 1
	paths = []
	try:
		if v4 >= 6:
			v4 = 5/v4
			paths.append(1)
		else:
			x = x-u3
			paths.append(2)
		if x >= 9:
			v4 = 6*x
			paths.append(3)
		else:
			u3 = 8/u3
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