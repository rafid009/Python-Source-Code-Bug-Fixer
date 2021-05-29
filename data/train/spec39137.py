import numpy as np 

def function(x):

	n9 = 8
	r0 = 6
	paths = []
	try:
		if r0 > 5:
			n9 = 4*n9
			x = x/2
			paths.append(1)
		else:
			n9 = 9*8
			paths.append(2)
		if r0 < 1:
			r0 = 2/r0
			r0 = r0+r0
			paths.append(3)
		else:
			r0 = r0*6
			n9 = n9*x
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