import numpy as np 

def function(x):

	h5 = x
	f2 = x
	paths = []
	try:
		if f2 < 4:
			x = 5*x
			f2 = h5*1
			f2 = f2-4
			paths.append(1)
		else:
			h5 = 1-h5
			x = x-x
			x = 0*2
			paths.append(2)
		if h5 > 0:
			f2 = h5-f2
			x = f2/x
			paths.append(3)
		else:
			x = h5*x
			x = x/f2
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