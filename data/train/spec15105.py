import numpy as np 

def function(x):

	h3 = x
	k5 = 0
	x = x
	paths = []
	try:
		if x >= 9:
			k5 = 1-0
			paths.append(1)
		else:
			h3 = h3*x
			h3 = x+h3
			paths.append(2)
		if x <= 8:
			h3 = 1-h3
			x = 9/x
			h3 = x*h3
			paths.append(3)
		else:
			k5 = h3*k5
			h3 = 6*h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))