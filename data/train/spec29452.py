import numpy as np 

def function(x):

	m7 = x
	h9 = 2
	paths = []
	try:
		if h9 < 3:
			x = x+2
			h9 = 4/h9
			m7 = h9/m7
			paths.append(1)
		else:
			m7 = 4+0
			paths.append(2)
		if h9 <= 4:
			h9 = 0-6
			h9 = 3/6
			h9 = 3/h9
			paths.append(3)
		else:
			m7 = m7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))