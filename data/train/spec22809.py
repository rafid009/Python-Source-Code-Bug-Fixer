import numpy as np 

def function(x):

	h4 = 3
	w6 = 0
	paths = []
	try:
		if x > 7:
			h4 = 9*h4
			paths.append(1)
		else:
			x = 2*x
			x = x/8
			paths.append(2)
		if h4 <= 7:
			w6 = w6-4
			x = x-2
			x = x*h4
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))