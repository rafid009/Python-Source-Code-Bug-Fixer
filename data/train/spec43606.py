import numpy as np 

def function(x):

	o9 = x
	h5 = x
	paths = []
	try:
		if h5 >= 3:
			o9 = o9+5
			x = x*1
			o9 = o9*x
			paths.append(1)
		else:
			o9 = o9/3
			h5 = h5-0
			paths.append(2)
		if h5 >= 3:
			x = 6-x
			x = x/3
			x = x*o9
			paths.append(3)
		else:
			o9 = 8+5
			x = 6+h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))