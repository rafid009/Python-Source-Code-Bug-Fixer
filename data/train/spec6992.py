import numpy as np 

def function(x):

	r1 = x
	h5 = x
	paths = []
	try:
		if x > 0:
			x = x+0
			x = x-3
			h5 = 7*h5
			paths.append(1)
		else:
			x = h5*h5
			h5 = h5+r1
			x = 0+r1
			paths.append(2)
		if h5 <= 3:
			r1 = x/8
			paths.append(3)
		else:
			r1 = 2*1
			h5 = 9-h5
			x = x-h5
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		r1 = h5**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))