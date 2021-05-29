import numpy as np 

def function(x):

	m0 = x
	h8 = 8
	paths = []
	try:
		if m0 > 5:
			m0 = m0-h8
			h8 = h8+5
			paths.append(1)
		else:
			x = x+h8
			h8 = m0+h8
			paths.append(2)
		if h8 >= 9:
			h8 = h8+5
			paths.append(3)
		else:
			x = 5-x
			h8 = h8/8
			m0 = 7*9
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))