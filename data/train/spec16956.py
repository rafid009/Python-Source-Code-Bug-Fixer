import numpy as np 

def function(x):

	k5 = 9
	q0 = 6
	paths = []
	try:
		if k5 < 3:
			q0 = q0-1
			x = 6*x
			paths.append(1)
		else:
			q0 = 0/6
			x = x/k5
			paths.append(2)
		if k5 >= 8:
			q0 = q0-4
			x = 9/q0
			k5 = k5-1
			paths.append(3)
		else:
			q0 = k5*5
			x = 7/k5
			x = x/x
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