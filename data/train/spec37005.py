import numpy as np 

def function(x):

	j8 = x
	k4 = x
	paths = []
	try:
		if k4 <= 1:
			k4 = 7-x
			paths.append(1)
		else:
			x = 9-k4
			paths.append(2)
		if j8 < 7:
			j8 = 0+j8
			x = j8*x
			paths.append(3)
		else:
			x = x-j8
			x = j8*x
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