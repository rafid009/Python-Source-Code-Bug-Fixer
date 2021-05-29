import numpy as np 

def function(x):

	q3 = 7
	c4 = x
	paths = []
	try:
		if q3 >= 7:
			q3 = 6/q3
			paths.append(1)
		else:
			x = x/5
			q3 = 9/x
			paths.append(2)
		if q3 >= 7:
			x = x+q3
			x = x*3
			paths.append(3)
		else:
			q3 = x/x
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