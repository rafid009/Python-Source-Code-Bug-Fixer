import numpy as np 

def function(x):

	a5 = x
	h1 = 7
	paths = []
	try:
		if h1 <= 6:
			a5 = a5+h1
			x = x-a5
			a5 = 6/h1
			paths.append(1)
		else:
			h1 = h1*4
			paths.append(2)
		if a5 <= 9:
			h1 = 0*h1
			a5 = a5*4
			h1 = h1-3
			paths.append(3)
		else:
			x = x+9
			h1 = 5/h1
			h1 = h1+h1
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