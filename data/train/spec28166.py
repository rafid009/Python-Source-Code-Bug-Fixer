import numpy as np 

def function(x):

	h2 = 7
	i4 = x
	paths = []
	try:
		if h2 <= 5:
			x = x*8
			x = 3*7
			h2 = 0+4
			paths.append(1)
		else:
			x = h2-x
			x = x+8
			h2 = h2+4
			paths.append(2)
		if h2 >= 5:
			i4 = 9-5
			i4 = 6+h2
			paths.append(3)
		else:
			x = 7-0
			h2 = h2*5
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