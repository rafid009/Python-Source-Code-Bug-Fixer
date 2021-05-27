import numpy as np 

def function(x):

	z0 = x
	r4 = 0
	paths = []
	try:
		if r4 < 1:
			r4 = x+r4
			paths.append(1)
		else:
			x = x+8
			r4 = r4-9
			paths.append(2)
		if x < 8:
			x = x-2
			x = x+3
			r4 = r4/r4
			paths.append(3)
		else:
			r4 = r4-x
			x = z0/x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		r4 = z0**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))