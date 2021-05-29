import numpy as np 

def function(x):

	n0 = 3
	r9 = 8
	paths = []
	try:
		if n0 < 6:
			r9 = n0+x
			x = 0*x
			paths.append(1)
		else:
			r9 = 6*8
			x = x-2
			r9 = r9*2
			paths.append(2)
		if r9 >= 2:
			n0 = r9-4
			r9 = r9/3
			r9 = r9-r9
			paths.append(3)
		else:
			n0 = 8+7
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))