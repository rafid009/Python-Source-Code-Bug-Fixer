import numpy as np 

def function(x):

	h2 = 8
	r6 = x
	paths = []
	try:
		if h2 < 5:
			x = x/2
			h2 = h2/h2
			paths.append(1)
		else:
			h2 = r6*5
			x = h2*7
			x = x/6
			paths.append(2)
		if x >= 5:
			r6 = r6/r6
			x = 8+x
			h2 = 0/h2
			paths.append(3)
		else:
			r6 = r6*x
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