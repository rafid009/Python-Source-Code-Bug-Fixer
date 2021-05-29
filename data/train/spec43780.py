import numpy as np 

def function(x):

	u4 = 0
	h1 = 7
	paths = []
	try:
		if u4 <= 4:
			u4 = h1-1
			paths.append(1)
		else:
			h1 = x*h1
			x = 2*x
			paths.append(2)
		if h1 >= 0:
			h1 = h1/9
			h1 = h1+4
			x = x-0
			paths.append(3)
		else:
			h1 = 3/h1
			u4 = 0*u4
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))