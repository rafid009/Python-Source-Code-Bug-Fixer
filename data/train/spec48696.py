import numpy as np 

def function(x):

	l4 = x
	h3 = x
	paths = []
	try:
		if h3 < 9:
			l4 = 1+l4
			x = x-l4
			paths.append(1)
		else:
			l4 = 6*0
			paths.append(2)
		if h3 >= 4:
			h3 = l4/x
			x = 7+7
			paths.append(3)
		else:
			x = 8+h3
			h3 = 3+h3
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