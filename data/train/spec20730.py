import numpy as np 

def function(x):

	d9 = 1
	h6 = x
	paths = []
	try:
		if h6 < 6:
			h6 = h6/9
			d9 = d9-d9
			x = x*h6
			paths.append(1)
		else:
			h6 = h6*h6
			d9 = d9+2
			x = 8+d9
			paths.append(2)
		if h6 >= 2:
			d9 = 0/x
			d9 = d9*x
			h6 = 5/8
			paths.append(3)
		else:
			x = 0/5
			d9 = d9/2
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))