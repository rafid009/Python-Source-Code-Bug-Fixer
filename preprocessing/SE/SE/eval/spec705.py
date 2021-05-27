import numpy as np 

def function(x):

	k4 = x
	j8 = 8
	paths = []
	try:
		if k4 >= 6:
			j8 = 6/j8
			x = x*8
			j8 = 2/j8
			paths.append(1)
		else:
			j8 = 9*j8
			x = x/1
			k4 = k4*6
			paths.append(2)
		if k4 >= 3:
			j8 = j8/7
			k4 = k4-3
			paths.append(3)
		else:
			x = x/x
			x = k4*j8
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