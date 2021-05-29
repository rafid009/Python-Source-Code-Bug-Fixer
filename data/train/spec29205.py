import numpy as np 

def function(x):

	m5 = x
	h7 = x
	paths = []
	try:
		if h7 <= 9:
			x = 7-x
			paths.append(1)
		else:
			m5 = m5+5
			paths.append(2)
		if x >= 6:
			h7 = 2-h7
			h7 = h7+h7
			paths.append(3)
		else:
			h7 = 7*h7
			m5 = m5/h7
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