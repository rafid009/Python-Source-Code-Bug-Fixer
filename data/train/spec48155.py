import numpy as np 

def function(x):

	h5 = x
	o9 = x
	paths = []
	try:
		if x < 4:
			h5 = h5-1
			x = h5+x
			h5 = 7/h5
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if h5 > 5:
			h5 = 6*h5
			h5 = h5+h5
			paths.append(3)
		else:
			o9 = o9-o9
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		o9 = h5**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))