import numpy as np 

def function(x):

	h4 = 9
	f0 = 1
	paths = []
	try:
		if h4 > 7:
			x = x-1
			paths.append(1)
		else:
			h4 = 8-h4
			x = f0-1
			paths.append(2)
		if h4 > 1:
			x = 1/x
			f0 = 3/f0
			paths.append(3)
		else:
			x = 5*x
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