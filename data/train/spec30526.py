import numpy as np 

def function(x):

	j5 = 1
	q3 = 2
	paths = []
	try:
		if x >= 2:
			q3 = 9+4
			x = x+6
			paths.append(1)
		else:
			j5 = 2/1
			paths.append(2)
		if j5 > 6:
			x = x-8
			paths.append(3)
		else:
			x = x+3
			q3 = 7/2
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