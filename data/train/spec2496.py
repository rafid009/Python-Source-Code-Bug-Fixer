import numpy as np 

def function(x):

	r0 = 8
	i0 = x
	paths = []
	try:
		if i0 < 5:
			i0 = 0-3
			paths.append(1)
		else:
			r0 = 2*i0
			x = r0-x
			r0 = 1+r0
			paths.append(2)
		if i0 > 6:
			x = x-3
			x = 3/8
			paths.append(3)
		else:
			r0 = r0-x
			r0 = r0/8
			r0 = i0*7
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