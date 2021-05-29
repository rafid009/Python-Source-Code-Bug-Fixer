import numpy as np 

def function(x):

	h4 = 8
	m0 = 3
	paths = []
	try:
		if m0 > 5:
			h4 = 8+4
			x = 2-h4
			paths.append(1)
		else:
			x = 6+x
			m0 = m0-6
			paths.append(2)
		if x <= 0:
			x = x*4
			paths.append(3)
		else:
			h4 = m0+3
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