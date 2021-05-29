import numpy as np 

def function(x):

	h4 = x
	a0 = 6
	paths = []
	try:
		if a0 <= 9:
			a0 = a0-x
			paths.append(1)
		else:
			h4 = 8/h4
			x = 0+h4
			paths.append(2)
		if x >= 9:
			h4 = h4+6
			paths.append(3)
		else:
			x = 5-a0
			a0 = 1-a0
			a0 = a0/h4
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		h4 = a0**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))