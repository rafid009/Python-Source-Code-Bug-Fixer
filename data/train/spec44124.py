import numpy as np 

def function(x):

	h5 = x
	f9 = 7
	paths = []
	try:
		if f9 > 1:
			h5 = 3+h5
			f9 = 3/3
			x = f9+x
			paths.append(1)
		else:
			x = x-f9
			paths.append(2)
		if h5 > 0:
			h5 = h5/3
			paths.append(3)
		else:
			h5 = 1/9
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))