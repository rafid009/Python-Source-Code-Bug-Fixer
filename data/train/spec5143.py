import numpy as np 

def function(x):

	h4 = x
	x6 = x
	paths = []
	try:
		if x >= 0:
			x = 5/x
			h4 = 1*h4
			x6 = x6+x
			paths.append(1)
		else:
			x = 1/x6
			paths.append(2)
		if x <= 5:
			x = x+2
			x = 9/2
			paths.append(3)
		else:
			h4 = 9*h4
			x6 = 1/5
			x6 = 8-x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		h4 = x6**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))