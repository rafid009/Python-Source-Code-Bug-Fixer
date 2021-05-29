import numpy as np 

def function(x):

	o6 = x
	h2 = 0
	x = 3
	paths = []
	try:
		if h2 >= 4:
			x = 8+2
			o6 = o6/9
			h2 = o6+h2
			paths.append(1)
		else:
			o6 = o6/9
			h2 = 9+h2
			paths.append(2)
		if h2 > 5:
			x = 1-x
			h2 = 0/2
			paths.append(3)
		else:
			x = o6/9
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		h2 = o6**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))