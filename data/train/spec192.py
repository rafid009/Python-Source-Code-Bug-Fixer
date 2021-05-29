import numpy as np 

def function(x):

	d1 = 7
	h5 = 7
	x = 8
	paths = []
	try:
		if x < 2:
			d1 = d1*2
			d1 = 4+2
			d1 = d1*x
			paths.append(1)
		else:
			d1 = 0+9
			h5 = h5-d1
			h5 = x/h5
			paths.append(2)
		if h5 <= 2:
			d1 = d1-2
			d1 = 4-8
			x = 7-h5
			paths.append(3)
		else:
			h5 = d1/5
			d1 = d1-x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		h5 = d1**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))