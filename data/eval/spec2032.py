import numpy as np 

def function(x):

	q0 = 9
	x4 = x
	paths = []
	try:
		if q0 >= 2:
			q0 = q0-9
			q0 = q0/7
			paths.append(1)
		else:
			q0 = 4/x4
			paths.append(2)
		if q0 <= 2:
			x4 = 3*x4
			x4 = x4/2
			paths.append(3)
		else:
			x = x4/x
			x = x+8
			x4 = x4+x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))