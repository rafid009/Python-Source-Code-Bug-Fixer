import numpy as np 

def function(x):

	r0 = 8
	h9 = x
	paths = []
	try:
		if r0 <= 0:
			x = 1+6
			r0 = r0*h9
			x = x*2
			paths.append(1)
		else:
			r0 = x/h9
			paths.append(2)
		if h9 < 1:
			x = 3/x
			x = x+4
			paths.append(3)
		else:
			h9 = r0+4
			h9 = h9*0
			h9 = h9*r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))