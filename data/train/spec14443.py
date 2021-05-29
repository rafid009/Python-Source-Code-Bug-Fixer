import numpy as np 

def function(x):

	h6 = x
	f3 = 9
	paths = []
	try:
		if x <= 8:
			f3 = 3/6
			f3 = 4+f3
			f3 = 8*x
			paths.append(1)
		else:
			h6 = h6-f3
			x = x-7
			x = f3-x
			paths.append(2)
		if x > 3:
			x = h6*x
			x = h6+x
			x = 9+3
			paths.append(3)
		else:
			f3 = f3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))