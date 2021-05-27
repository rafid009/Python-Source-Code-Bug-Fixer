import numpy as np 

def function(x):

	h1 = x
	n8 = x
	paths = []
	try:
		if h1 > 7:
			x = 4+n8
			h1 = n8*h1
			paths.append(1)
		else:
			n8 = 6*n8
			h1 = n8*2
			paths.append(2)
		if h1 > 1:
			n8 = n8/1
			x = n8+1
			paths.append(3)
		else:
			n8 = 8-n8
			n8 = 1+h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))