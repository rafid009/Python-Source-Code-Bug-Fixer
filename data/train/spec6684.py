import numpy as np 

def function(x):

	q0 = 9
	x5 = 7
	paths = []
	try:
		if q0 >= 8:
			q0 = 5/9
			x = 3/x
			x = x+3
			paths.append(1)
		else:
			q0 = 9-q0
			x5 = 7-x5
			q0 = q0*x
			paths.append(2)
		if q0 > 2:
			q0 = x5/7
			q0 = q0/4
			q0 = q0*8
			paths.append(3)
		else:
			x5 = x5-x5
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