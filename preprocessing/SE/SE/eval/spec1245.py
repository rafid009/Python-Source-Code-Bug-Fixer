import numpy as np 

def function(x):

	r4 = 2
	h2 = x
	paths = []
	try:
		if r4 >= 1:
			h2 = h2+5
			paths.append(1)
		else:
			x = h2*9
			h2 = 8-x
			paths.append(2)
		if x < 7:
			x = x+4
			r4 = r4+2
			x = 2/x
			paths.append(3)
		else:
			r4 = r4/2
			h2 = 0+h2
			r4 = r4*r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))