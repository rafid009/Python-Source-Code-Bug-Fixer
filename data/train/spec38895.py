import numpy as np 

def function(x):

	m2 = 4
	h8 = x
	paths = []
	try:
		if x <= 2:
			m2 = 3+3
			h8 = h8/4
			paths.append(1)
		else:
			m2 = 0/h8
			m2 = h8+m2
			paths.append(2)
		if h8 < 4:
			x = x/3
			paths.append(3)
		else:
			m2 = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))