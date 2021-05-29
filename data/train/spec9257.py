import numpy as np 

def function(x):

	q0 = x
	e9 = 5
	paths = []
	try:
		if q0 > 2:
			e9 = q0+e9
			paths.append(1)
		else:
			x = x-q0
			paths.append(2)
		if q0 >= 2:
			e9 = e9-q0
			e9 = 5+e9
			x = e9+x
			paths.append(3)
		else:
			e9 = e9-1
			x = 2*x
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