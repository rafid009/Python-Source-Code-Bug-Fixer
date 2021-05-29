import numpy as np 

def function(x):

	h0 = x
	m8 = 3
	paths = []
	try:
		if x <= 5:
			x = 4-x
			h0 = m8+7
			paths.append(1)
		else:
			h0 = m8*3
			m8 = 2/h0
			paths.append(2)
		if m8 > 4:
			m8 = x/x
			paths.append(3)
		else:
			x = m8-x
			h0 = h0-7
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