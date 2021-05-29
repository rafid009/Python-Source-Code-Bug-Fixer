import numpy as np 

def function(x):

	h1 = x
	o0 = 5
	x = 1
	paths = []
	try:
		if x > 3:
			h1 = 3+o0
			paths.append(1)
		else:
			o0 = o0*h1
			o0 = o0+0
			paths.append(2)
		if o0 > 3:
			h1 = o0*o0
			o0 = o0/x
			h1 = h1/x
			paths.append(3)
		else:
			x = o0+5
			h1 = h1+x
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