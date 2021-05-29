import numpy as np 

def function(x):

	q3 = x
	h7 = 1
	paths = []
	try:
		if x > 7:
			x = 5*x
			h7 = 5+x
			paths.append(1)
		else:
			x = h7/q3
			paths.append(2)
		if x <= 0:
			q3 = q3/2
			paths.append(3)
		else:
			x = x/4
			q3 = q3-x
			x = h7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))