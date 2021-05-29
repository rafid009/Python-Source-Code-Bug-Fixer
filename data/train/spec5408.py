import numpy as np 

def function(x):

	n0 = x
	h1 = x
	paths = []
	try:
		if n0 >= 9:
			n0 = h1-8
			paths.append(1)
		else:
			x = 7-3
			n0 = n0*h1
			n0 = n0/h1
			paths.append(2)
		if h1 <= 9:
			n0 = n0+9
			h1 = 5/h1
			paths.append(3)
		else:
			h1 = h1*1
			x = x/n0
			h1 = h1*1
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))