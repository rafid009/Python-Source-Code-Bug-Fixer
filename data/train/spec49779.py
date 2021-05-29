import numpy as np 

def function(x):

	h4 = x
	m4 = x
	paths = []
	try:
		if h4 < 5:
			m4 = 1*m4
			h4 = h4-m4
			paths.append(1)
		else:
			h4 = x+h4
			h4 = 1+h4
			paths.append(2)
		if x <= 0:
			h4 = h4+6
			h4 = x+1
			paths.append(3)
		else:
			x = 0/5
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