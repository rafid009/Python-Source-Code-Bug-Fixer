import numpy as np 

def function(x):

	h7 = 3
	r0 = x
	paths = []
	try:
		if x > 7:
			x = 2*9
			paths.append(1)
		else:
			h7 = h7/9
			r0 = 5*r0
			paths.append(2)
		if h7 > 9:
			x = 7-7
			x = x/x
			h7 = x/h7
			paths.append(3)
		else:
			x = x*9
			h7 = 1+r0
			r0 = r0-8
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