import numpy as np 

def function(x):

	m9 = 9
	h3 = 1
	paths = []
	try:
		if h3 < 9:
			m9 = 4/m9
			h3 = m9-h3
			x = 5/x
			paths.append(1)
		else:
			h3 = h3*5
			h3 = 8+x
			paths.append(2)
		if m9 >= 7:
			h3 = 8+7
			h3 = 2+3
			h3 = x-1
			paths.append(3)
		else:
			x = 4+8
			x = m9/x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))