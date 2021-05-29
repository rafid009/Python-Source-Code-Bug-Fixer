import numpy as np 

def function(x):

	j3 = x
	n0 = x
	paths = []
	try:
		if x >= 0:
			n0 = j3+n0
			paths.append(1)
		else:
			n0 = 8+n0
			x = x-2
			n0 = n0+4
			paths.append(2)
		if x >= 7:
			n0 = 6-1
			j3 = n0*9
			j3 = 8+n0
			paths.append(3)
		else:
			n0 = n0*j3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))