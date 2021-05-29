import numpy as np 

def function(x):

	j8 = 6
	j0 = 5
	paths = []
	try:
		if x > 1:
			j0 = 6-j0
			j8 = 6/j0
			paths.append(1)
		else:
			j8 = 7-j8
			j8 = j8-7
			j0 = 3/j8
			paths.append(2)
		if x > 7:
			x = x-3
			paths.append(3)
		else:
			x = x+x
			x = 9/j0
			x = 2+x
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