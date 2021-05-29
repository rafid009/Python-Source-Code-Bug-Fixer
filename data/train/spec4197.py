import numpy as np 

def function(x):

	q6 = x
	x7 = x
	x = 8
	paths = []
	try:
		if x > 9:
			x7 = x7/1
			paths.append(1)
		else:
			q6 = 2/q6
			x = x-9
			x7 = 6/x7
			paths.append(2)
		if x > 6:
			x = 1/x
			q6 = q6/9
			paths.append(3)
		else:
			x7 = x7+x7
			x7 = q6-x7
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