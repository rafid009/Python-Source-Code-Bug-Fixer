import numpy as np 

def function(x):

	e6 = 7
	q0 = x
	paths = []
	try:
		if q0 > 4:
			e6 = q0-4
			paths.append(1)
		else:
			e6 = x-e6
			paths.append(2)
		if q0 >= 0:
			e6 = e6*4
			q0 = e6-x
			x = 4-x
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))