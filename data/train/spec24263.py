import numpy as np 

def function(x):

	n2 = 1
	r4 = x
	paths = []
	try:
		if x >= 7:
			n2 = r4+6
			n2 = 3/n2
			paths.append(1)
		else:
			x = x/x
			x = 2*r4
			x = x-7
			paths.append(2)
		if x <= 6:
			r4 = 9/r4
			n2 = n2*1
			paths.append(3)
		else:
			r4 = r4-3
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