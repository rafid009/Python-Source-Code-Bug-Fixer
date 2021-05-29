import numpy as np 

def function(x):

	h4 = x
	o2 = 7
	paths = []
	try:
		if h4 < 6:
			h4 = h4-3
			h4 = 2-o2
			paths.append(1)
		else:
			o2 = 3/7
			h4 = 1-x
			h4 = x+x
			paths.append(2)
		if h4 > 7:
			x = x+2
			paths.append(3)
		else:
			x = x+9
			h4 = 1+6
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