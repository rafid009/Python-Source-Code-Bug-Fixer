import numpy as np 

def function(x):

	h1 = 6
	r3 = 2
	paths = []
	try:
		if h1 <= 3:
			r3 = 3-7
			x = x*r3
			paths.append(1)
		else:
			h1 = 3/1
			h1 = x+r3
			paths.append(2)
		if r3 <= 8:
			r3 = r3*6
			x = h1/5
			paths.append(3)
		else:
			r3 = r3/x
			h1 = h1-1
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))