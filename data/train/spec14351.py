import numpy as np 

def function(x):

	x3 = 0
	r9 = x
	paths = []
	try:
		if x > 5:
			x3 = x3-8
			paths.append(1)
		else:
			r9 = r9-x3
			x3 = 9-x3
			paths.append(2)
		if x > 1:
			r9 = r9/x
			paths.append(3)
		else:
			x3 = x-0
			x = r9-x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))