import numpy as np 

def function(x):

	a5 = x
	h1 = 7
	paths = []
	try:
		if h1 <= 3:
			x = 6*x
			a5 = a5*2
			x = 5*h1
			paths.append(1)
		else:
			a5 = x+a5
			a5 = a5/2
			paths.append(2)
		if a5 >= 8:
			x = x-h1
			paths.append(3)
		else:
			a5 = a5-3
			h1 = h1-h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))