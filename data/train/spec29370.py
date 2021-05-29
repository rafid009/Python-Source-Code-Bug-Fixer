import numpy as np 

def function(x):

	a0 = 8
	r0 = x
	paths = []
	try:
		if x < 0:
			r0 = r0*7
			x = r0-8
			paths.append(1)
		else:
			a0 = a0-r0
			r0 = 6*8
			x = 1-x
			paths.append(2)
		if x < 0:
			r0 = r0-8
			a0 = 9*r0
			a0 = a0+1
			paths.append(3)
		else:
			x = 5/a0
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