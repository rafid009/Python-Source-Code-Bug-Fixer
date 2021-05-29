import numpy as np 

def function(x):

	h5 = x
	m0 = x
	paths = []
	try:
		if x < 6:
			h5 = m0+h5
			h5 = h5+8
			m0 = h5-1
			paths.append(1)
		else:
			x = 3-m0
			x = 6+3
			h5 = h5+h5
			paths.append(2)
		if x < 2:
			x = x+8
			paths.append(3)
		else:
			h5 = 5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))