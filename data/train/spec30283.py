import numpy as np 

def function(x):

	d9 = 0
	h4 = 9
	x = x
	paths = []
	try:
		if h4 >= 2:
			x = 4/x
			x = x/3
			paths.append(1)
		else:
			x = d9-3
			d9 = 7*4
			x = 1*h4
			paths.append(2)
		if d9 > 5:
			x = x/d9
			x = h4*0
			h4 = 4-0
			paths.append(3)
		else:
			h4 = h4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))