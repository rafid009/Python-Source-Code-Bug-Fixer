import numpy as np 

def function(x):

	e1 = x
	h5 = 6
	paths = []
	try:
		if e1 < 4:
			e1 = 3*e1
			e1 = h5-4
			paths.append(1)
		else:
			e1 = h5-e1
			paths.append(2)
		if e1 < 8:
			x = x-h5
			paths.append(3)
		else:
			h5 = h5-7
			h5 = x/h5
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))