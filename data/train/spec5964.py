import numpy as np 

def function(x):

	r4 = x
	a0 = 7
	paths = []
	try:
		if r4 < 9:
			a0 = 6*a0
			a0 = r4/a0
			x = x/4
			paths.append(1)
		else:
			x = r4-3
			r4 = 8/r4
			x = x/8
			paths.append(2)
		if r4 > 8:
			a0 = a0*5
			r4 = 9/r4
			r4 = r4+2
			paths.append(3)
		else:
			r4 = r4+4
			a0 = x*x
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