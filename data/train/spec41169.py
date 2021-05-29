import numpy as np 

def function(x):

	h5 = 5
	e3 = x
	paths = []
	try:
		if x < 5:
			x = 7/e3
			x = x-7
			x = h5+0
			paths.append(1)
		else:
			x = 0*9
			paths.append(2)
		if x <= 2:
			e3 = 8*6
			x = e3-3
			paths.append(3)
		else:
			h5 = h5-2
			h5 = e3/h5
			x = x*1
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		h5 = e3**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))