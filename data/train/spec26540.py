import numpy as np 

def function(x):

	h4 = 6
	m4 = x
	paths = []
	try:
		if x >= 2:
			h4 = 5/2
			h4 = 5/x
			m4 = h4/m4
			paths.append(1)
		else:
			m4 = 0-m4
			m4 = h4/x
			x = x*h4
			paths.append(2)
		if m4 <= 5:
			x = h4*7
			paths.append(3)
		else:
			m4 = 6/m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		h4 = m4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))