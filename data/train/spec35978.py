import numpy as np 

def function(x):

	h7 = 9
	r1 = 5
	paths = []
	try:
		if x > 8:
			x = x/3
			r1 = r1/3
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if r1 >= 0:
			h7 = h7-7
			x = x-0
			paths.append(3)
		else:
			h7 = r1-h7
			h7 = h7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))