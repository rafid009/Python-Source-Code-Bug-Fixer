import numpy as np 

def function(x):

	x7 = x
	v6 = x
	paths = []
	try:
		if x < 9:
			x = 7*x
			v6 = 1-v6
			paths.append(1)
		else:
			x7 = 1/x
			paths.append(2)
		if v6 >= 9:
			x7 = x7*9
			x7 = x7/v6
			paths.append(3)
		else:
			x = 7*x
			x = 3-1
			x7 = 1*x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))