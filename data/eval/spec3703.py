import numpy as np 

def function(x):

	r3 = x
	h3 = x
	paths = []
	try:
		if r3 < 6:
			h3 = h3/8
			h3 = h3*9
			h3 = 0-h3
			paths.append(1)
		else:
			r3 = 6-r3
			paths.append(2)
		if r3 >= 4:
			x = 3-9
			x = x-7
			paths.append(3)
		else:
			x = 7-x
			r3 = 7/r3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		r3 = h3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))