import numpy as np 

def function(x):

	x7 = 7
	r2 = 4
	paths = []
	try:
		if r2 >= 0:
			r2 = 4-x7
			paths.append(1)
		else:
			x7 = 3/x7
			r2 = 5-r2
			paths.append(2)
		if r2 >= 0:
			x = x+9
			x7 = x7-1
			paths.append(3)
		else:
			x7 = r2/x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))