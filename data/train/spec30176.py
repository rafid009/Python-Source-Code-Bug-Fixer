import numpy as np 

def function(x):

	e9 = 6
	h5 = 3
	paths = []
	try:
		if x < 5:
			x = x+8
			paths.append(1)
		else:
			e9 = x+2
			x = x-3
			paths.append(2)
		if x < 2:
			x = h5*2
			paths.append(3)
		else:
			h5 = e9-9
			h5 = h5+0
			x = x/3
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		e9 = h5**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))