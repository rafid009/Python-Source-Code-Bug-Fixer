import numpy as np 

def function(x):

	a1 = x
	h2 = x
	paths = []
	try:
		if x >= 3:
			x = 1/x
			a1 = h2*a1
			paths.append(1)
		else:
			a1 = a1-5
			h2 = h2+h2
			paths.append(2)
		if a1 > 4:
			a1 = a1-5
			paths.append(3)
		else:
			x = 7*x
			a1 = 8+h2
			a1 = 6*a1
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