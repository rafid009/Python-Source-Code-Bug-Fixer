import numpy as np 

def function(x):

	h1 = 9
	n4 = x
	paths = []
	try:
		if h1 >= 0:
			h1 = h1/3
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if h1 <= 7:
			n4 = h1*x
			paths.append(3)
		else:
			x = n4-7
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))