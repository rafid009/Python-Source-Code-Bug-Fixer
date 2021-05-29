import numpy as np 

def function(x):

	v7 = x
	h1 = x
	paths = []
	try:
		if h1 <= 8:
			x = 4*x
			paths.append(1)
		else:
			v7 = 9/v7
			h1 = h1+v7
			paths.append(2)
		if x >= 6:
			h1 = v7-h1
			paths.append(3)
		else:
			h1 = 2/9
			v7 = 5+v7
			x = x*h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))