import numpy as np 

def function(x):

	h5 = 6
	o4 = 9
	paths = []
	try:
		if o4 <= 4:
			o4 = x/9
			x = 0+0
			h5 = 4-h5
			paths.append(1)
		else:
			h5 = 2+h5
			h5 = h5/o4
			o4 = o4*1
			paths.append(2)
		if h5 > 1:
			h5 = x*h5
			x = 7-x
			paths.append(3)
		else:
			o4 = h5*o4
			o4 = o4-h5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))