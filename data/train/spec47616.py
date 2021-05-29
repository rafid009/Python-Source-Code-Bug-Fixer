import numpy as np 

def function(x):

	o4 = x
	h2 = 0
	paths = []
	try:
		if x <= 0:
			h2 = 8-x
			o4 = x+o4
			h2 = h2-x
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if h2 > 9:
			x = x/8
			paths.append(3)
		else:
			o4 = x/o4
			o4 = h2-o4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))