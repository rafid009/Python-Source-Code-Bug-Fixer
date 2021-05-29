import numpy as np 

def function(x):

	h5 = 4
	f0 = 6
	x = x
	paths = []
	try:
		if h5 <= 2:
			f0 = 8-3
			h5 = x-3
			x = f0+f0
			paths.append(1)
		else:
			f0 = 5-x
			paths.append(2)
		if x > 9:
			f0 = x-9
			f0 = f0-7
			x = 3/x
			paths.append(3)
		else:
			f0 = 6*6
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))