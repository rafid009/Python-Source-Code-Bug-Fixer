import numpy as np 

def function(x):

	r1 = 7
	n0 = 8
	paths = []
	try:
		if r1 < 8:
			r1 = 7*6
			n0 = 0/x
			paths.append(1)
		else:
			r1 = r1-r1
			paths.append(2)
		if n0 >= 4:
			n0 = n0+1
			x = x+7
			x = n0/2
			paths.append(3)
		else:
			r1 = r1-2
			r1 = 3/r1
			n0 = n0+8
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