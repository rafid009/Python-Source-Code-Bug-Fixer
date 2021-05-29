import numpy as np 

def function(x):

	a8 = x
	h1 = 5
	paths = []
	try:
		if h1 > 3:
			a8 = 8-0
			a8 = a8-2
			a8 = a8*6
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if a8 <= 0:
			x = 8-x
			paths.append(3)
		else:
			a8 = a8+x
			h1 = 5+h1
			x = h1/x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		h1 = a8**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))