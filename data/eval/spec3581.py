import numpy as np 

def function(x):

	n4 = 6
	k4 = 3
	paths = []
	try:
		if x < 4:
			k4 = 1*k4
			paths.append(1)
		else:
			n4 = 8*k4
			paths.append(2)
		if n4 > 4:
			n4 = n4-1
			paths.append(3)
		else:
			k4 = n4/1
			n4 = n4*n4
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