import numpy as np 

def function(x):

	f1 = x
	h1 = x
	paths = []
	try:
		if x > 5:
			f1 = f1+f1
			paths.append(1)
		else:
			h1 = h1*h1
			f1 = f1/4
			f1 = 6*f1
			paths.append(2)
		if f1 < 9:
			h1 = h1+0
			paths.append(3)
		else:
			x = x-h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))