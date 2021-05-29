import numpy as np 

def function(x):

	h5 = x
	e1 = 4
	paths = []
	try:
		if x > 4:
			e1 = h5-7
			x = 0-7
			h5 = h5/1
			paths.append(1)
		else:
			x = x*5
			h5 = h5/h5
			paths.append(2)
		if h5 <= 3:
			e1 = e1-5
			paths.append(3)
		else:
			e1 = e1-4
			e1 = x+e1
			e1 = 6/e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		h5 = e1**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))