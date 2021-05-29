import numpy as np 

def function(x):

	h5 = 0
	y3 = 6
	paths = []
	try:
		if x < 1:
			x = 7*x
			y3 = y3-x
			paths.append(1)
		else:
			x = y3/6
			x = x*2
			x = 2+y3
			paths.append(2)
		if h5 >= 4:
			h5 = h5*h5
			paths.append(3)
		else:
			h5 = 7+h5
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))