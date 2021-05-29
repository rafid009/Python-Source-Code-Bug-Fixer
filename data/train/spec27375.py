import numpy as np 

def function(x):

	h1 = x
	n1 = x
	x = x
	paths = []
	try:
		if x < 9:
			h1 = 0*x
			n1 = n1/1
			paths.append(1)
		else:
			n1 = 5/n1
			x = x+3
			x = 7+n1
			paths.append(2)
		if h1 < 1:
			h1 = h1+h1
			paths.append(3)
		else:
			h1 = h1+n1
			n1 = 1*n1
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