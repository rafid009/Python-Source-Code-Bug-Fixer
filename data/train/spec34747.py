import numpy as np 

def function(x):

	x4 = x
	x3 = 5
	paths = []
	try:
		if x3 < 2:
			x4 = 8+1
			x = x-x3
			paths.append(1)
		else:
			x3 = 4+x3
			x3 = x3*x
			x3 = x3/8
			paths.append(2)
		if x3 < 5:
			x3 = 9+1
			x3 = 9*4
			x3 = 2*x
			paths.append(3)
		else:
			x3 = 2/x3
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