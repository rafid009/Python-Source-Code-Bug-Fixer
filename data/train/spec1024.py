import numpy as np 

def function(x):

	e3 = 0
	h5 = x
	paths = []
	try:
		if x < 1:
			x = 5+h5
			paths.append(1)
		else:
			h5 = e3*x
			paths.append(2)
		if e3 < 7:
			e3 = e3*4
			paths.append(3)
		else:
			h5 = e3-e3
			h5 = h5-3
			x = h5*4
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		e3 = h5**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))