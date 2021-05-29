import numpy as np 

def function(x):

	a0 = 5
	r2 = 2
	paths = []
	try:
		if r2 >= 3:
			x = 3/a0
			x = 0+6
			paths.append(1)
		else:
			a0 = a0-a0
			a0 = 4*4
			a0 = a0+7
			paths.append(2)
		if a0 >= 0:
			r2 = x-0
			a0 = a0+x
			r2 = r2/r2
			paths.append(3)
		else:
			a0 = 6/a0
			r2 = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))