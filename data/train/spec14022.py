import numpy as np 

def function(x):

	h5 = 3
	k6 = x
	paths = []
	try:
		if x <= 4:
			k6 = 3/x
			paths.append(1)
		else:
			x = k6*1
			k6 = 9*8
			paths.append(2)
		if k6 >= 2:
			h5 = h5-0
			paths.append(3)
		else:
			x = x/3
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