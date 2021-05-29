import numpy as np 

def function(x):

	h2 = x
	q0 = 1
	paths = []
	try:
		if x < 0:
			q0 = 4*x
			q0 = q0/8
			q0 = x+4
			paths.append(1)
		else:
			q0 = q0*8
			q0 = q0+4
			paths.append(2)
		if h2 > 1:
			h2 = h2+9
			paths.append(3)
		else:
			q0 = 9*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))