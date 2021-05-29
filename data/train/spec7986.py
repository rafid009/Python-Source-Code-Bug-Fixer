import numpy as np 

def function(x):

	h7 = 4
	m6 = x
	paths = []
	try:
		if h7 <= 5:
			h7 = h7*4
			h7 = 1-m6
			x = h7*x
			paths.append(1)
		else:
			h7 = h7-x
			paths.append(2)
		if x <= 8:
			x = x-6
			x = 5*x
			paths.append(3)
		else:
			x = x+9
			x = 9*x
			m6 = 0+h7
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