import numpy as np 

def function(x):

	n4 = x
	q6 = 5
	paths = []
	try:
		if x < 2:
			n4 = x/5
			q6 = x/q6
			paths.append(1)
		else:
			q6 = q6+5
			n4 = 2/x
			paths.append(2)
		if x > 3:
			x = 1/5
			paths.append(3)
		else:
			n4 = 3+n4
			q6 = x*q6
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