import numpy as np 

def function(x):

	r0 = 8
	i0 = x
	paths = []
	try:
		if r0 >= 4:
			x = 4/7
			r0 = 2/r0
			r0 = 9*r0
			paths.append(1)
		else:
			x = x+i0
			r0 = 6/2
			paths.append(2)
		if r0 >= 1:
			r0 = r0*5
			x = x+i0
			paths.append(3)
		else:
			r0 = 5/r0
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