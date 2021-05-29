import numpy as np 

def function(x):

	h3 = x
	p8 = 6
	paths = []
	try:
		if h3 <= 1:
			h3 = h3-9
			p8 = h3+4
			paths.append(1)
		else:
			h3 = h3/x
			paths.append(2)
		if x < 4:
			p8 = p8+8
			h3 = 8/h3
			x = 9*x
			paths.append(3)
		else:
			h3 = x*h3
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		h3 = p8**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))