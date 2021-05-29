import numpy as np 

def function(x):

	f2 = x
	h9 = x
	paths = []
	try:
		if f2 >= 9:
			h9 = 9+h9
			paths.append(1)
		else:
			x = x*f2
			paths.append(2)
		if h9 > 4:
			h9 = h9-h9
			h9 = f2+f2
			x = 6*x
			paths.append(3)
		else:
			x = x+h9
			f2 = f2/f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))