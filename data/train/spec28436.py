import numpy as np 

def function(x):

	m0 = x
	h7 = 0
	paths = []
	try:
		if m0 > 2:
			h7 = h7*4
			x = x-h7
			paths.append(1)
		else:
			h7 = 8*6
			h7 = x*h7
			paths.append(2)
		if h7 < 0:
			x = 1+x
			paths.append(3)
		else:
			x = 5*7
			h7 = m0*h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))