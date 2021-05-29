import numpy as np 

def function(x):

	h4 = 3
	x0 = 9
	paths = []
	try:
		if h4 < 5:
			h4 = h4*8
			x0 = x0/3
			x0 = 8+x0
			paths.append(1)
		else:
			h4 = h4-x0
			x = 1/7
			h4 = h4+3
			paths.append(2)
		if x <= 4:
			x0 = 5+0
			x0 = x0/x
			paths.append(3)
		else:
			x = x*6
			x0 = x0+6
			h4 = 3*h4
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))