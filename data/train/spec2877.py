import numpy as np 

def function(x):

	h6 = x
	r8 = 7
	paths = []
	try:
		if x < 8:
			r8 = 2-r8
			h6 = 8*7
			r8 = 8-r8
			paths.append(1)
		else:
			x = x-5
			h6 = h6*r8
			paths.append(2)
		if x > 1:
			h6 = h6+1
			paths.append(3)
		else:
			r8 = r8*x
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