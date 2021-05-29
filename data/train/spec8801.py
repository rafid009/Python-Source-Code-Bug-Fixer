import numpy as np 

def function(x):

	h5 = x
	o7 = 7
	paths = []
	try:
		if h5 > 1:
			x = 7/1
			x = h5+1
			paths.append(1)
		else:
			o7 = 0-o7
			h5 = 4-1
			h5 = h5*o7
			paths.append(2)
		if o7 >= 2:
			h5 = h5+8
			h5 = 7-h5
			h5 = 6+h5
			paths.append(3)
		else:
			x = x*o7
			x = x/9
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		o7 = h5**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))