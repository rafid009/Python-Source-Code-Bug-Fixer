import numpy as np 

def function(x):

	x7 = x
	r9 = x
	paths = []
	try:
		if r9 >= 1:
			x7 = 7/x7
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x7 >= 6:
			r9 = 3+x
			r9 = r9-x
			paths.append(3)
		else:
			x7 = 0-x7
			x = 4-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))