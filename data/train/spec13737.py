import numpy as np 

def function(x):

	m6 = x
	h4 = x
	paths = []
	try:
		if m6 < 6:
			h4 = h4-9
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x < 0:
			h4 = h4+0
			paths.append(3)
		else:
			h4 = h4/m6
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		h4 = m6**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))