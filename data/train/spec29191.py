import numpy as np 

def function(x):

	c8 = x
	j0 = x
	paths = []
	try:
		if x >= 2:
			j0 = 3/8
			j0 = j0-4
			paths.append(1)
		else:
			x = 4/c8
			j0 = j0+1
			paths.append(2)
		if c8 <= 5:
			j0 = 5*j0
			x = 3*8
			paths.append(3)
		else:
			j0 = j0+3
			x = x-c8
			j0 = 9/j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))