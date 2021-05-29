import numpy as np 

def function(x):

	h2 = 4
	h4 = x
	x = 4
	paths = []
	try:
		if x > 4:
			h2 = h2/6
			h4 = 3+h4
			paths.append(1)
		else:
			h4 = 2+h4
			paths.append(2)
		if h2 >= 1:
			h4 = h4+1
			h4 = h4*8
			paths.append(3)
		else:
			h4 = h4+9
			h2 = h4-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))