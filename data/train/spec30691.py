import numpy as np 

def function(x):

	n7 = 9
	d9 = 9
	paths = []
	try:
		if x >= 1:
			x = 3/3
			paths.append(1)
		else:
			d9 = d9+0
			n7 = d9+n7
			x = x+4
			paths.append(2)
		if d9 > 1:
			n7 = n7*n7
			n7 = d9+x
			d9 = 0*d9
			paths.append(3)
		else:
			x = d9-7
			x = 0-x
			d9 = 7*d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))