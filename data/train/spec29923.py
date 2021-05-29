import numpy as np 

def function(x):

	r2 = 2
	x5 = x
	paths = []
	try:
		if x5 > 3:
			x5 = 5*x5
			x5 = 8*x5
			x = 8/x
			paths.append(1)
		else:
			r2 = x5-r2
			x = 3-x
			paths.append(2)
		if r2 >= 9:
			x = x5*x5
			paths.append(3)
		else:
			r2 = 8/4
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))