import numpy as np 

def function(x):

	h6 = 6
	q0 = 1
	paths = []
	try:
		if q0 <= 0:
			x = x*x
			q0 = 5+x
			paths.append(1)
		else:
			h6 = x+q0
			paths.append(2)
		if h6 < 7:
			q0 = q0-x
			x = q0+2
			q0 = q0+h6
			paths.append(3)
		else:
			x = x+q0
			x = h6-x
			x = 2*x
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