import numpy as np 

def function(x):

	h3 = 8
	i6 = 4
	paths = []
	try:
		if i6 <= 5:
			x = x-i6
			i6 = i6-3
			paths.append(1)
		else:
			h3 = 1+h3
			x = i6-6
			paths.append(2)
		if h3 >= 6:
			h3 = 1/h3
			h3 = h3-h3
			i6 = i6/8
			paths.append(3)
		else:
			x = 3*x
			h3 = 3*h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))