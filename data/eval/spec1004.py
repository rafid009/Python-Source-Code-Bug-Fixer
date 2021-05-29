import numpy as np 

def function(x):

	e8 = x
	h5 = 7
	paths = []
	try:
		if e8 >= 5:
			x = x*5
			x = 1-x
			paths.append(1)
		else:
			x = 3-x
			e8 = e8+1
			h5 = 7*e8
			paths.append(2)
		if e8 < 1:
			x = x/x
			e8 = e8+3
			paths.append(3)
		else:
			h5 = h5+7
			e8 = 3/3
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))